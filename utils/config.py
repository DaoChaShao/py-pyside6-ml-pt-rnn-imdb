#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:38
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   config.py
# @Desc     :   

from dataclasses import dataclass, field
from pathlib import Path
from torch import cuda

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass
class FilePaths:
    MODEL: Path = BASE_DIR / "models/model.pth"
    SPACY_EN_MODEL = BASE_DIR / "models/spacy/en_core_web_md"
    SPACY_ZH_MODEL = BASE_DIR / "models/spacy/zh_core_web_md"
    STANZA_MODEL = BASE_DIR / "models/stanza"
    DATASET_TRAIN = BASE_DIR / "data/train/"
    DATASET_TEST = BASE_DIR / "data/test/"
    DICTIONARY = BASE_DIR / "data/dictionary.json"


@dataclass
class DataPreprocessor:
    PCA_VARIANCE_THRESHOLD: float = 0.95
    RANDOM_STATE: int = 27
    VALID_SIZE: float = 0.7
    IS_SHUFFLE: bool = True
    BATCH_SIZE: int = 32


@dataclass
class ModelParameters:
    FC_HIDDEN_UNITS: int = 128
    DROPOUT_RATE: float = 0.3
    RNN_SEQ_MAX_LEN: int = 12
    RNN_EMBEDDING_DIM: int = 256
    RNN_HIDDEN_SIZE: int = 512
    RNN_LAYERS: int = 3
    RNN_TEMPERATURE: float = 1.0


@dataclass
class Hyperparameters:
    ALPHA: float = 1e-3
    EPOCHS: int = 20
    ACCELERATOR: str = "cuda" if cuda.is_available() else "cpu"


@dataclass
class Configration:
    FILEPATHS: FilePaths = field(default_factory=FilePaths)
    PREPROCESSOR: DataPreprocessor = field(default_factory=DataPreprocessor)
    PARAMETERS: ModelParameters = field(default_factory=ModelParameters)
    HYPERPARAMETERS: Hyperparameters = field(default_factory=Hyperparameters)


CONFIG = Configration()
