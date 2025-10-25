#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:22
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from utils.nlp import snlp_analysis


def main() -> None:
    """ Main Function """
    text_zh = "这是一个用于测试自然语言处理功能的示例文本."
    text_en = "This is a sample text for testing natural language processing features."
    snlp_analysis(text_zh, language="zh")


if __name__ == "__main__":
    main()
