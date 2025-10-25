#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:46
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   nlp.py
# @Desc     :   

from collections import Counter
from os import path
from pathlib import Path
from re import compile, sub
from pandas import DataFrame
from stanza import Pipeline, download

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
    pattern = compile(r"[A-Za-z]+")

    english: list[str] = [word for word in words if pattern.match(word)]

    print(f"Retained {len(english)} English words from the original {len(words)} words.")

    return english


@timer
def count_words_frequency(words: list[str], top_k: int = 10) -> tuple[list, DataFrame]:
    """ Get frequency of Chinese words
    :param words: list of words to process
    :param top_k: number of top frequent words to return
    :return: DataFrame containing words and their frequencies
    """
    # Get word frequency using Counter
    counter = Counter(words)
    words: list[str] = [word for word, count in counter.most_common()]

    cols: list[str] = ["word", "frequency"]
    sorted_freq = counter.most_common(top_k)
    df: DataFrame = DataFrame(sorted_freq, columns=cols)
    sorted_df = df.sort_values(by="frequency", ascending=False)

    print(f"Word Frequency Results:\n{sorted_df}")

    return words, sorted_df


@timer
def snlp_analysis(content: str, mode: str = "cut", language: str = "en", is_gpu: bool = False) -> list[str]:
    """ Perform part-of-speech tagging using StanfordNLP
    :param content: text content to process
    :param mode: processing mode, e.g., 'cut' for word segmentation, 'pos' for get words and their pos, 'full' for full text processing,
    :param language: language code for the text (default is 'zh' for Chinese, 'en' for English)
    :param is_gpu: whether to use GPU for processing (default is False)
    :return: list of tuples containing words and their corresponding POS tags
    """
    """
    The weights_only in PyTorch 2.6 and later versions defaults to True.
    However, StanfordNLP model files require weights_only=False.
    If you plan to use StanfordNLP, you MUST set weights_only=False and downgrade to PyTorch 2.5 or earlier versions.
    """
    # Download the necessary models if not already downloaded
    root_dir = path.dirname(path.abspath(__file__))
    model_dir = path.join(root_dir, "models")
    download(language, model_dir=model_dir)

    # Set up the processors based on the mode
    processors: str = "tokenize,lemma"
    match mode:
        case "cut":
            processors: str = "tokenize,lemma"
        case "pos":
            processors: str = "tokenize,lemma,pos"
    # Initialize the StanfordNLP pipeline
    nlp = Pipeline(processors=processors, lang=language, use_gpu=is_gpu, download_method=None)
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

    print(f"The {len(words)} words has been {mode} using StanfordNLP Text Analysis.")

    return words


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
