#!/usr/bin/env python3
import copy


class Path:
    path = []

    def __init__(self, path):
        self.path = path

    def add(self, board):
        self.path.append(board)

    def clone(self):
        return copy.deepcopy(self.path)

    def last(self):
        return self.path[-1]