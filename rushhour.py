#!/usr/bin/env python3

from board import Board
import sys

x = Board("  o aa|  o   |xxo   |ppp  q|     q|     q")
arguments = sys.argv
if len(arguments) == 2:
        firstArg = arguments[1]
        cars = []
        for row in x.board:
                for car in row:
                        if car not in cars and car != " ":
                                cars.append(car)
        if firstArg == "print":
                x.printBoard()
        elif firstArg == "done":
                d = x.done()
                print(d)
        elif firstArg == "next":
                for car in cars:
                        x.next_for_car(car)
                x.printBoards()
        elif firstArg == "random":
                x.random()
        elif firstArg == "bfs":
                x.bfs()
elif len(arguments) == 3:
        firstArg = arguments[1]
        secArg = arguments[2]
        y = Board(secArg)
        cars = []
        for row in y.board:
                for car in row:
                        if car not in cars and car != " ":
                                cars.append(car)
        if firstArg == "print":
                y.printBoard()
        elif firstArg == "done":
                d = y.done()
                print(d)
        elif firstArg == "next":
                for car in cars:
                        y.next_for_car(car)
                y.printBoards()
        elif firstArg == "random":
                y.random()
        elif firstArg == "bfs":
                y.bfs()
