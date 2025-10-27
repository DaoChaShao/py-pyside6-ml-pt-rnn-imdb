#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/25 18:40
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   models.py
# @Desc     :   

from torch import nn, relu
from torchsummary import summary


class RNNClassificationTorchModel(nn.Module):
    """ AN RNN model for multi-class classification tasks using PyTorch """

    def __init__(
            self,
            vocab_size: int, embedding_dim: int, hidden_size: int, num_layers: int,
            num_classes: int, dropout_rate: float = 0.3
    ):
        super().__init__()
        """ Initialise the CharsRNNModel class
        :param vocab_size: size of the vocabulary
        :param embedding_dim: dimension of the embedding layer
        :param hidden_dim: dimension of the hidden layer
        :param num_layers: number of RNN layers
        :param num_classes: number of output classes
        :param dropout_rate: dropout rate for regularization
        """
        self._L = vocab_size  # Lexicon/Vocabulary size
        self._N = embedding_dim  # Embedding dimension
        self._M = hidden_size  # Hidden dimension
        self._C = num_layers  # RNN layers count

        self._embed = nn.Embedding(self._L, self._N)
        self._lstm = nn.LSTM(self._N, self._M, self._C, batch_first=True, dropout=dropout_rate, bidirectional=True)
        self.dropout = nn.Dropout(dropout_rate)
        self._fc = nn.Linear(self._M * 2, num_classes)

        self._init_params()

    def _init_params(self):
        """ Initialize model parameters """
        for name, param in self.named_parameters():
            if "weight" in name:
                nn.init.xavier_uniform_(param)
            elif "bias" in name:
                nn.init.zeros_(param)

    def forward(self, X, hx=None):
        """ Forward pass of the model
        :param X: input tensor, shape (batch_size, sequence_length)
        :param hx: hidden state tensor, shape (num_layers, batch_size, hidden_dim)
        :return: output tensor and new hidden state tensor, shapes (batch_size, sequence_length, vocab_size) and (num_layers, batch_size, hidden_dim)
        """
        out = self._embed(X)
        out, hn = self._lstm(out, hx) if hx is not None else self._lstm(out)
        # Take the output of the last time step, shape (batch_size, hidden_dim)
        out = out[:, -1, :]
        # Fully connected layer, shape (batch_size, num_classes)
        out = self._fc(out)

        return out

    def summary(self):
        """ Print the model summary """
        print("=" * 64)
        total_params = sum(p.numel() for p in self.parameters())
        trainable_params = sum(p.numel() for p in self.parameters() if p.requires_grad)
        print(f"Model Summary for {self.__class__.__name__}")
        print("-" * 64)
        print(f"- Vocabulary size: {self._L}")
        print(f"- Embedding dim: {self._N}")
        print(f"- Hidden size: {self._M}")
        print(f"- Num layers: {self._C}")
        print(f"- Output classes: {self._fc.out_features}")
        print(f"- Total parameters: {total_params:,}")
        print(f"- Trainable parameters: {trainable_params:,}")
        print("=" * 64)
        print()


if __name__ == "__main__":
    pass
