#!/usr/bin/env python3

from board import Board
import sys

x = Board("  o aa|  o   |xxo   |ppp  q|     q|     q")
arguments = sys.argv
if len(arguments) == 2:
	firstArg = arguments[1]
	if firstArg == "print":
		x.print()
	elif firstArg == "done":
		x.done()
	elif firstArg == "next":
		rows = x.boardString.split("|")
		cars = []
		for row in rows:
			cs = list(row)
			for car in cs:
				if car not in cars and car != " ":
					cars.append(car)
		for car in cars:
			x.next_for_car(car)
		x.printBoards()
elif len(arguments) == 3:
	firstArg = arguments[1]
	secArg = arguments[2]
	y = Board(secArg)
	if firstArg == "print":
		y.print()
	elif firstArg == "done":
		y.done()
	elif firstArg == "next":
		rows = y.boardString.split("|")
		cars = []
		for row in rows:
			cs = list(row)
			for car in cs:
				if car not in cars and car != " ":
					cars.append(car)
		for car in cars:
			y.next_for_car(car)
		y.printBoards()
