#!/usr/bin/env python3
import copy
import random
from path import Path

class Board:
    board = []
    boards = []
    g = 0
    h = 0
    f = g + h

    def __init__(self, board):
        if type(board) is str:
            setup = board.split("|")
            b = []
            for i in range(len(setup)):
                s = list(setup[i])
                b.append(s)
            self.board = b
        else:
            self.board = board

    def printBoard(self):
        b = " ------ "
        setup = self.board
        for i in range(len(setup)):
            b += "\n"
            s = "".join(setup[i])
            b += "|" + s
            if i != 2:
                b += "|"
        b += "\n"
        b += " ------ "
        print(b)

    def printBoards(self):
        sep = " ------ "
        length = len(self.boards)
        output = ""
        for i in range(length):
            output += sep + " "
        height = len(self.board)
        for j in list(range(height)):
            output += "\n"
            for board in self.boards:
                output += "|" + "".join(board[j])
                if j != 2:
                    output += "| "
                else:
                    output += "  "
        output += "\n"
        for i in range(length):
            output += sep + " "
        print(output)

    def done(self):
        rows = self.board
        impRow = rows[2]
        lastBit = impRow[-1]
        if lastBit == "x":
            return True
        else:
            return False

    def getLastIndex(self, arr, car):
        index = 0
        for i in range(len(arr)):
            curr = arr[i]
            if car in curr:
                index = i
        return index

    def swapPositions(self, l, pos1, pos2):
        l[pos1], l[pos2] = l[pos2], l[pos1]
        return l

    def next_for_car(self, car, path):
        if path == None:
            rows = copy.deepcopy(self.board)
        else:
            rows = copy.deepcopy(path)
        for i in range(len(rows)):
            row = copy.copy(rows[i])
            if car in row and row.count(car) > 1:
                directions = list(range(2))
                for direction in directions:
                    r = copy.copy(row)
                    firstCarIndex = row.index(car)
                    lastCarIndex = len(row) - 1 - row[::-1].index(car)
                    obstacle = False
                    if direction == 0:
                        while not obstacle:
                            lastCarIndex += 1
                            if lastCarIndex >= len(r):
                                obstacle = True
                            elif r[lastCarIndex] == " ":
                                r = self.swapPositions(r, firstCarIndex, lastCarIndex)
                                h = copy.copy(r)
                                firstCarIndex += 1
                                rows[i] = h
                                if rows not in self.boards and rows != self.board:
                                    self.boards.append(copy.copy(rows))
                                    return copy.copy(rows)
                            else:
                                obstacle = True
                    elif direction == 1:
                        while not obstacle:
                            firstCarIndex -= 1
                            if firstCarIndex < 0:
                                obstacle = True
                            elif r[firstCarIndex] == " ":
                                r = self.swapPositions(r, firstCarIndex, lastCarIndex)
                                h = copy.copy(r)
                                lastCarIndex -= 1
                                rows[i] = h
                                if rows not in self.boards and rows != self.board:
                                    self.boards.append(copy.copy(rows))
                                    return copy.copy(rows)
                            else:
                                obstacle = True
            elif car in row and row.count(car) == 1:
                j = list(range(2))
                r = copy.copy(row)
                carIndex = r.index(car)
                amtRows = len(rows) - 1
                for direction in j:
                    firstRowIndex = rows.index(row)
                    lastRowIndex = self.getLastIndex(rows, car)
                    obstacle = False
                    while not obstacle:
                        if direction == 0:
                            lastRowIndex += 1
                            if lastRowIndex > amtRows:
                                obstacle = True
                            elif rows[lastRowIndex][carIndex] == car:
                                continue
                            elif rows[lastRowIndex][carIndex] == " ":
                                r = rows[firstRowIndex]
                                k = rows[lastRowIndex]
                                r[carIndex] = " "
                                k[carIndex] = car
                                h = copy.copy(r)
                                d = copy.copy(k)
                                rows[firstRowIndex] = d
                                rows[lastRowIndex] = h
                                lastRowIndex = self.getLastIndex(rows, car)
                                if rows not in self.boards and rows != self.board:
                                    self.boards.append(copy.copy(rows))
                                    return copy.copy(rows)
                            else:
                                obstacle = True
                                return None
                        elif direction == 1:
                            firstRowIndex -= 1
                            if firstRowIndex < 0:
                                obstacle = True
                            elif rows[firstRowIndex][carIndex] == car:
                                continue
                            elif rows[firstRowIndex][carIndex] == " ":
                                r = copy.copy(rows[firstRowIndex])
                                k = copy.copy(rows[lastRowIndex])
                                r[carIndex] = car
                                k[carIndex] = " "
                                h = copy.copy(r)
                                d = copy.copy(k)
                                rows[firstRowIndex] = h
                                rows[lastRowIndex] = d
                                lastRowIndex = self.getLastIndex(rows, car)
                                if rows not in self.boards and rows != self.board:
                                    self.boards.append(copy.copy(rows))
                                    return copy.copy(rows)
                            else:
                                obstacle = True
                                return None

    def nextPath(self, car, path):
        if path == None:
            rows = copy.deepcopy(self.board)
        else:
            rows = copy.deepcopy(path)
        for i in range(len(rows)):
            row = copy.copy(rows[i])
            if car in row and row.count(car) > 1:
                directions = list(range(2))
                index = random.randrange(len(directions))
                direction = directions[index]
                r = copy.copy(row)
                firstCarIndex = row.index(car)
                lastCarIndex = len(row) - 1 - row[::-1].index(car)
                obstacle = False
                if direction == 0:
                    while not obstacle:
                        lastCarIndex += 1
                        if lastCarIndex >= len(r):
                            obstacle = True
                        elif r[lastCarIndex] == " ":
                            r = self.swapPositions(r, firstCarIndex, lastCarIndex)
                            h = copy.copy(r)
                            firstCarIndex += 1
                            rows[i] = h
                            if rows not in self.boards and rows != self.board:
                                self.boards.append(copy.copy(rows))
                                return copy.copy(rows)
                        else:
                            obstacle = True
                elif direction == 1:
                    while not obstacle:
                        firstCarIndex -= 1
                        if firstCarIndex < 0:
                            obstacle = True
                        elif r[firstCarIndex] == " ":
                            r = self.swapPositions(r, firstCarIndex, lastCarIndex)
                            h = copy.copy(r)
                            lastCarIndex -= 1
                            rows[i] = h
                            if rows not in self.boards and rows != self.board:
                                self.boards.append(copy.copy(rows))
                                return copy.copy(rows)
                        else:
                            obstacle = True
            elif car in row and row.count(car) == 1:
                r = copy.copy(row)
                carIndex = r.index(car)
                amtRows = len(rows) - 1
                directions = list(range(2))
                index = random.randrange(len(directions))
                direction = directions[index]
                firstRowIndex = rows.index(row)
                lastRowIndex = self.getLastIndex(rows, car)
                obstacle = False
                while not obstacle:
                    if direction == 0:
                        lastRowIndex += 1
                        if lastRowIndex > amtRows:
                            return None
                        elif rows[lastRowIndex][carIndex] == " ":
                            r = copy.copy(rows[firstRowIndex])
                            k = copy.copy(rows[lastRowIndex])
                            r[carIndex] = " "
                            k[carIndex] = car
                            firstRowIndex += 1
                            if rows not in self.boards and rows != self.board:
                                self.boards.append(copy.copy(rows))
                                return copy.copy(rows)
                        else:
                            return None
                    elif direction == 1:
                        firstRowIndex -= 1
                        if firstRowIndex < 0:
                            obstacle = True
                        elif rows[firstRowIndex][carIndex] == car:
                            continue
                        elif rows[firstRowIndex][carIndex] == " ":
                            r = copy.copy(rows[firstRowIndex])
                            k = copy.copy(rows[lastRowIndex])
                            r[carIndex] = car
                            k[carIndex] = " "
                            h = copy.copy(r)
                            d = copy.copy(k)
                            rows[firstRowIndex] = h
                            rows[lastRowIndex] = d
                            lastRowIndex -= 1
                            if rows not in self.boards and rows != self.board:
                                self.boards.append(copy.copy(rows))
                                return copy.copy(rows)
                        else:
                            return None

    def random(self, moves=10):
        path = Path()
        cars = []
        for row in self.board:
            for car in row:
                if car not in cars and car != " ":
                    cars.append(car)
        for move in range(moves):
            index = random.randrange(len(cars))
            car = cars[index]
            nextPath = self.nextPath(car, path.last())
            if nextPath != None:
                path.add(nextPath)
        self.boards = path.path
        self.printBoards()

    def bfs(self):
        path = Path()
        start = Board(copy.deepcopy(self.board))
        cars = []
        for row in start.board:
            for car in row:
                if car not in cars and car != " ":
                    cars.append(car)
        visited = []
        queue = [start]
        done = False
        while len(queue) != 0:
            node = queue.pop(0)
            visited.append(node)
            for car in cars:
                nextPath = self.nextPath(car, path.last())
                if nextPath != None:
                    check = Board(nextPath)
                    if check.done():
                        done = True
                        return node
                    if nextPath not in visited:
                        path.add(nextPath)
                        queue.append(nextPath)
        self.printBoards()
        return len(path.path)

    def getH(self):
        board = self.board
        for i in range(len(board)):
            if "x" in board[i]:
                for car in list(board[i]):
                    return abs(list(board[i]).index(car) - len(list(board[i])) + 1)

    def astar(self):
        path = Path()
        open = [copy.deepcopy(self.board)]
        closed = []
        i = 0
        cars = []
        for row in self.board:
            for car in row:
                if car not in cars and car != " ":
                    cars.append(car)
        while len(open) != 0:
            node = open.pop(0)
            h = self.getH()
            g = i
            f = h + g
            i += 1
            for car in cars:
                nextPath = self.nextPath(car, path.last())
                if nextPath not in closed:
                    open.append(nextPath)
                if h == 0:
                    return node
                else:
                    closed.append(node)
        self.printBoards()
        print(len(self.boards))


if __name__ == '__main__':
    b = Board("  o aa|  o   |xxo   |ppp  q|     q|     q")
    cars = []
    for row in b.board:
        for car in row:
            if car not in cars and car != " ":
                cars.append(car)
    b.astar()