#!/usr/bin/env python3
import copy


class Path:
    path = []
    max_boards = 6

    def __init__(self, path=[]):
        self.path = path

    def add(self, board):
        self.path.append(board)

    def clone(self):
        return copy.deepcopy(self.path)

    def last(self):
        if len(self.path) > 0:
            return self.path[-1]
        else:
            return None