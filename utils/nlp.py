#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:46
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   nlp.py
# @Desc     :   

from collections import Counter
from pathlib import Path
from re import compile, sub
from pandas import DataFrame
from spacy import load
from stanza import Pipeline

from utils.config import CONFIG
from utils.decorator import timer


@timer
def regular_chinese(words: list[str]) -> list[str]:
    """ Retain only Chinese characters in the list of words
    :param words: list of words to process
    :return: list of words containing only Chinese characters
    """
    pattern = compile(r"[\u4e00-\u9fa5]+")

    chinese: list[str] = [word for word in words if pattern.match(word)]

    print(f"Retained {len(chinese)} Chinese words from the original {len(words)} words.")

    return chinese


@timer
def regular_english(words: list[str]) -> list[str]:
    """ Retain only English characters in the list of words
    :param words: list of words to process
    :return: list of words containing only English characters
    """
    pattern = compile(r"^[A-Za-z]+$")

    english: list[str] = [word.lower() for word in words if pattern.match(word)]

    print(f"Retained {len(english)} English words from the original {len(words)} words.")

    return english


@timer
def count_frequency(words: list[str], top_k: int = 10, freq_threshold: int = 3) -> tuple[list, DataFrame]:
    """ Get frequency of Chinese words
    :param words: list of words to process
    :param top_k: number of top frequent words to return
    :param freq_threshold: frequency threshold to separate high and low frequency words
    :return: DataFrame containing words and their frequencies
    """
    # Get word frequency using Counter
    counter = Counter(words)
    words_high_freq: list[str] = [word for word, count in counter.most_common() if count > freq_threshold]
    words_low_freq: list[str] = [word for word, count in counter.most_common() if count <= freq_threshold]

    cols: list[str] = ["word", "frequency"]
    sorted_freq = counter.most_common(top_k)
    df: DataFrame = DataFrame(sorted_freq, columns=cols)
    sorted_df = df.sort_values(by="frequency", ascending=False)

    print(f"Word Frequency Results:\n{sorted_df}")
    print(f"{len(words_low_freq)} low frequency words has been filtered out (frequency <= {freq_threshold}).")

    return words_high_freq, sorted_df


@timer
def unique_characters(content: str) -> list[str]:
    """ Get unique words from the list
    :param content: text content to process
    :return: list of unique words
    """
    chars: list[str] = list(content)
    # Get unique words by converting the list to a set and back to a sorted list
    # - sort based on Unicode code point order
    unique: list[str] = list(sorted(set(chars)))

    print(f"Extracted {len(unique)} unique words from the original {len(chars)} words.")

    return unique


@timer
def extract_zh_chars(filepath: str | Path, pattern: str = r"[^\u4e00-\u9fa5]") -> tuple[list, list]:
    """ Get Chinese characters from the text content
    :param filepath: path to the text file
    :param pattern: regex pattern to remove unwanted characters
    :return: list of Chinese characters
    """
    chars: list[str] = []
    lines: list[str] = []
    with open(str(filepath), "r", encoding="utf-8") as file:
        for line in file:
            line = sub(pattern, "", line).strip()
            if not line:
                continue
            lines.append(line)
            for word in list(line):
                chars.append(word)

    print(f"Total number of Chinese characters: {len(chars)}")
    print(f"Total number of lines in the Chinese content: {len(lines)}")

    return chars, lines


def spacy_tokeniser(content: str, lang: str) -> list[str]:
    """ SpaCy NLP Processor for an English or a Chinese text
    :param content: a text content to process
    :param lang: language code for the text (e.g., 'en' for English, 'zh' for Chinese)
    :return: list of tokens
    """
    words: list[str] = []
    match lang:
        case "en":
            nlp = load(CONFIG.FILEPATHS.SPACY_EN_MODEL)
            doc = nlp(content)
            words = [token.lemma_.lower() for token in doc]
        case "zh":
            nlp = load(CONFIG.FILEPATHS.SPACY_ZH_MODEL)
            doc = nlp(content)
            words = [token.text for token in doc]
        case _:
            raise ValueError(f"Unsupported language: {lang}")

    print(f"The {len(words)} words has been segmented using SpaCy Tokeniser.")

    return words


@timer
def stanza_tokeniser(content: str, mode: str = "cut", lang: str = "en", is_gpu: bool = False) -> list[str]:
    """ Perform part-of-speech tagging using StanfordNLP, which is called Stanza now
    :param content: text content to process
    :param mode: processing mode, e.g., 'cut' for word segmentation, 'pos' for get words and their pos, 'full' for full text processing,
    :param lang: language code for the text (default is 'zh' for Chinese, 'en' for English)
    :param is_gpu: whether to use GPU for processing (default is False)
    :return: list of tuples containing words and their corresponding POS tags
    """
    # Set up the processors based on the mode
    processors: str = "tokenize,lemma"
    match mode:
        case "cut":
            processors: str = "tokenize,lemma"
        case "pos":
            processors: str = "tokenize,lemma,pos"
    # Initialize the StanfordNLP pipeline
    nlp = Pipeline(
        processors=processors,
        lang=lang,
        use_gpu=is_gpu,
        model_dir=str(CONFIG.FILEPATHS.STANZA_MODEL),
        download_method=None,
    )
    # Process the content
    doc = nlp(content)

    words_tuple: list[tuple[str] | tuple[str, str] | tuple[str, str, str]] = []
    # Extract words and their POS tags
    for sentence in doc.sentences:
        for word in sentence.words:
            match processors:
                case "tokenize,lemma":
                    words_tuple.append((word.text.lower(),))
                case "tokenize,lemma,pos":
                    words_tuple.append((word.text.lower(), word.upos))

    words: list[str] = [word[0] for word in words_tuple]

    print(f"The {len(words)} words has been {mode} using StanfordNLP/Stanza Tokeniser.")

    return words
