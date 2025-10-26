#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:22
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from tqdm import tqdm

from utils.config import CONFIG
from utils.helper import load_text_data_in_dir, save_json
from utils.nlp import spacy_tokeniser, regular_english, count_frequency
from utils.PT import LabelTorchDataset, TorchDataLoader
from utils.stats import split_data


def tokenize_texts(texts: list[str]) -> list[list[str]]:
    """ Tokenize a list of texts using spaCy
    :param texts: list of texts to tokenize
    :return: list of tokenized texts
    """
    new: list[list[str]] = []
    for text in tqdm(texts, total=len(texts), desc="Tokenizing texts"):
        words = spacy_tokeniser(text, "en")
        words = regular_english(words)
        new.append(words)
    return new


def build_word2id_seqs(contents: list[list[str]], dictionary: dict[str, int]) -> list[list[int]]:
    """ Build word2id sequences from contents using the provided dictionary
    :param contents: list of texts to convert
    :param dictionary: word2id mapping dictionary
    :return: list of word2id sequences
    """
    sequences: list[list[int]] = []
    for content in contents:
        sequence: list[int] = []
        for word in content:
            if word in dictionary:
                sequence.append(dictionary[word])
            else:
                sequence.append(dictionary["<UNK>"])
        sequences.append(sequence)
    return sequences


def check_seq_coverage(dictionary: dict, test_seqs: list) -> float:
    """ Check vocabulary coverage of the dictionary on the test sequences
    :param dictionary: word2id mapping dictionary
    :param test_seqs: list of test sequences
    :return: coverage percentage of known tokens in the dictionary
    """
    total_tokens = sum(len(seq) for seq in test_seqs)
    known_tokens = sum(1 for seq in test_seqs for token in seq if token in dictionary)
    coverage = known_tokens / total_tokens * 100

    print(f"The known tokens occupied {coverage:.2%} of the dictionary.")
    print(f"The know tokens: {known_tokens}/{total_tokens}")

    return coverage


def preprocess_data():
    """ Data Preprocessing Function """
    # Load dataset
    train = load_text_data_in_dir(CONFIG.FILEPATHS.DATASET_TRAIN)
    test = load_text_data_in_dir(CONFIG.FILEPATHS.DATASET_TEST)
    # index = randint(0, len(train["ids"]) - 1)
    # print(f"Train | ID: {train["ids"][index]}, Rate: {train["ratings"][index]}, Label: {train["labels"][index]}")
    # print(f"Test  | ID: {test["ids"][index]}, Rate: {test["ratings"][index]}, Label: {test["labels"][index]}")
    # print(f"Train | Labels: {train["labels"][12495:12505]}")
    # print(f"Test  | Labels: {test["labels"][12495:12505]}")

    # Tokenize texts
    amount: int | None = 10
    content_train: list[list[str]] = tokenize_texts(train["contents"][: amount])
    label_train: list[list[int]] = train["labels"][: amount]
    # print(len(content_train), content_train)
    # print(len(content_train))
    content_test: list[list[str]] = tokenize_texts(test["contents"][: amount])
    label_test: list[list[int]] = test["labels"][: amount]

    # Spilt validation set from test set
    content_valid, content_test, label_valid, label_test = split_data(
        content_test, label_test,
        valid_size=CONFIG.PREPROCESSOR.VALID_SIZE,
        random_state=CONFIG.PREPROCESSOR.RANDOM_STATE,
        is_shuffle=CONFIG.PREPROCESSOR.IS_SHUFFLE
    )

    # Count frequency
    contents = content_train + content_valid
    unique_words = [word for content in contents for word in content]
    freq_words, _ = count_frequency(unique_words, top_k=10)
    # print(freq_words)

    # Create a dictionary/word2id mapping words to indices
    special: list[str] = ["<PAD>", "<UNK>"]
    dictionary: dict[str, int] = {word: idx for idx, word in enumerate(special + freq_words)}
    # print(dictionary)
    save_json(dictionary, CONFIG.FILEPATHS.DICTIONARY)

    # Build 2D index representation of texts
    sequences: list[list[int]] = build_word2id_seqs(contents, dictionary)
    # print(sequences)

    # Padding the sequences to a fixed length
    lengths: list[int] = [len(seq) for seq in sequences]
    max_len = max(lengths)
    min_len = min(lengths)
    avg_len = sum(lengths) / len(lengths)
    print(f"Max Length: {max_len}, Min Length: {min_len}, Avg Length: {avg_len:.2f}")

    # Setup features and labels
    X_train: list[list[int]] = build_word2id_seqs(content_train, dictionary)
    X_valid: list[list[int]] = build_word2id_seqs(content_valid, dictionary)
    X_test: list[list[int]] = build_word2id_seqs(content_test, dictionary)
    y_train: list[list[int]] = label_train
    y_valid: list[list[int]] = label_valid
    y_test: list[list[int]] = label_test
    # print(f"{len(X_train)} X Train: {X_train}")
    # print(f"{len(y_train)} y Train: {y_train}")
    # print(f"{len(X_valid)} X Valid: {X_valid}")
    # print(f"{len(y_valid)} y Valid: {y_valid}")
    # print(f"{len(X_test)} X Test: {X_test}")
    # print(f"{len(y_test)} y Test: {y_test}")

    return X_train, y_train, X_valid, y_valid, X_test, y_test


def prepare_dataset():
    """ Dataset Preparation Function """
    X_train, y_train, X_valid, y_valid, _, _ = preprocess_data()

    # Create PyTorch Datasets
    train_dataset = LabelTorchDataset(X_train, y_train)
    valid_dataset = LabelTorchDataset(X_valid, y_valid)

    # Create DataLoaders
    train_loader = TorchDataLoader(
        dataset=train_dataset,
        batch_size=CONFIG.PREPROCESSOR.BATCH_SIZE,
        is_shuffle=CONFIG.PREPROCESSOR.IS_SHUFFLE,
    )
    valid_loader = TorchDataLoader(
        dataset=valid_dataset,
        batch_size=CONFIG.PREPROCESSOR.BATCH_SIZE,
        is_shuffle=CONFIG.PREPROCESSOR.IS_SHUFFLE,
    )

    print(f"Number of training batches: {len(train_loader)}")
    print(f"Number of validation batches: {len(valid_loader)}")

    return train_loader, valid_loader


def main() -> None:
    """ Main Function """
    prepare_dataset()


if __name__ == "__main__":
    main()
