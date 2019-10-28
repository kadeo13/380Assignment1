#!/usr/bin/env python3
import copy

class Board:
    board = []
    boards = []

    def __init__(self, board):
        setup = board.split("|")
        b = []
        for i in range(len(setup)):
            s = list(setup[i])
            b.append(s)
        self.board = b

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

    def next_for_car(self, car):
        rows = copy.deepcopy(self.board)
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
                            firstRowIndex += 1
                            if firstRowIndex > amtRows:
                                obstacle = True
                            elif rows[firstRowIndex][carIndex] == car:
                                continue
                            elif rows[firstRowIndex][carIndex] == " ":
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
                            else:
                                obstacle = True
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
                            else:
                                obstacle = True

    def random(self):
        pass

if __name__ == '__main__':
    b = Board("  ooo |ppp q |xx  qa|rrr qa|b c dd|b c ee")
    rows = b.board
    cars = []
    for row in rows:
        for car in row:
            if car not in cars and car != " ":
                cars.append(car)
    for car in cars:
        b.next_for_car(car)
    b.printBoards()