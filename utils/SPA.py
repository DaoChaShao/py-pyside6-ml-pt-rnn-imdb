#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:44
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   SPA.py
# @Desc     :   

from spacy import load

from utils.decorator import Timer


@Timer("Tokenize and lemmatize English text using SpaCy")
class SpaCyNLP:
    """ SpaCy NLP Processor for English text
    - download the small model
        - pip: python -m spacy download en_core_web_sm
        - uv:
    - download the medium model
        - pip: python -m spacy download en_core_web_md
    - download the large model
        - pip: python -m spacy download en_core_web_lg
    """

    def __init__(self, content: str):
        """ Initialize SpaCy NLP Processor
        :param content: The text to be tokenized.
        """
        self._nlp = load("en_core_web_lg")
        self._doc = self._nlp(content)

    def __call__(self) -> list:
        """ Tokenize English text using spacy package into words.
        :return: List of tokens.
        """
        return [token.lemma_ for token in self._doc]
