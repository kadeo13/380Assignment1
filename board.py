#!/usr/bin/env python3

class Board:
	boardString = ""
	boards = []

	def __init__(self, board):
		self.boardString = board

	def print(self):
		board = " ------ "
		setup = self.boardString.split("|")
		for i in range(len(setup)):
			board += "\n"
			board += "|" + setup[i]
			if i != 2:
				board += "|"
		board += "\n"
		board += " ------ "
		print(board)
	
	def printBoards(self):
		sep = " ------ "
		length = len(self.boards)
		output = ""
		for i in range(length):
			output += sep + " "
		width = len(list(self.boardString.split("|")[0]))	
		for j in list(range(width)):
			output += "\n"
			for board in self.boards:
				b = board.split("|")
				output += "|" + b[j]
				if j != 2:
					output += "| "
				else:
					output += "  "
		output += "\n"
		for i in range(length):
			output += sep + " "
		print(output)
	
	def getLastIndex(self, arr, car):
		index = 0
		for i in range(len(arr)):
			curr = arr[i]
			if car in curr:
				index = i
		return index
	
	def getFirstIndex(self, arr, car):
		i = 0
		for i in range(len(arr)):
			curr = arr[i]
			if car in curr:
				return i
	
	def swapPositions(self, l, pos1, pos2):
		l[pos1], l[pos2] = l[pos2], l[pos1]
		return l
	
	def next_for_car(self, car):
		rows = self.boardString.split("|")
		for i in range(len(rows)):
			row = rows[i]
			h = list(row)
			if car in row and h.count(car) > 1:
				j = list(range(2))
				for direction in j:
					r = h
					firstCarIndex = r.index(car)
					lastCarIndex = len(r) - 1 - r[::-1].index(car)
					obstacle = False
					if direction == 0:
						while not obstacle:
							lastCarIndex += 1
							if lastCarIndex > 5:
								obstacle = True
								break
							elif r[lastCarIndex] == " ":
								r = self.swapPositions(r, firstCarIndex, lastCarIndex)
								hold = rows
								delim = ""
								row = delim.join(r)
								hold[i] = row
								delim = "|"
								string = delim.join(hold)
								firstCarIndex += 1
								if string not in self.boards and string != self.boardString:
									self.boards.append(string)
							else:
								obstacle = True
					elif direction == 1:
						while not obstacle:
							firstCarIndex -= 1
							if firstCarIndex < 0:
								obstacle = True
								break
							elif r[firstCarIndex] == " ":
								r = self.swapPositions(r, firstCarIndex, lastCarIndex)
								hold = rows
								delim = ""
								row = delim.join(r)
								hold[i] = row
								delim = "|"
								string = delim.join(hold)
								lastCarIndex -= 1
								if string not in self.boards and string != self.boardString:
									self.boards.append(string)
							else:
								obstacle = True
			elif car in row:
				j = list(range(2))
				r = h
				carIndex = r.index(car)
				rowIndex = rows.index(row)
				amtRows = len(rows) - 1
				ogIndex = self.getLastIndex(rows, car)
				for direction in j:
					obstacle = False
					while not obstacle:
						if direction == 0:
							rowIndex += 1
							if rowIndex > amtRows:
								obstacle = True
								break
							elif list(rows[rowIndex])[carIndex] == car:
								continue
							elif list(rows[rowIndex])[carIndex] == " ":
								hold = rows
								delim = ""
								r = list(hold[rowIndex])
								k = list(hold[ogIndex])
								k[carIndex] = " "
								r[carIndex] = car
								rrow = delim.join(r)
								krow = delim.join(k)
								delim = "|"
								hold[rowIndex] = rrow
								hold[ogIndex] = krow
								string = delim.join(hold)
								ogIndex = self.getLastIndex(rows, car)
								if string not in self.boards and string != self.boardString:
									self.boards.append(string)
							else:
								obstacle = True
						elif direction == 1:
							rowIndex -= 1
							if rowIndex < 0:
								obstacle = True
								break
							elif list(rows[rowIndex])[carIndex] == car:
								continue
							elif list(rows[rowIndex])[carIndex] == " ":
								hold = rows
								delim = ""
								r = list(hold[rowIndex])
								k = list(hold[ogIndex])
								k[carIndex] = " "
								r[carIndex] = car
								rrow = delim.join(r)
								krow = delim.join(k)
								delim = "|"
								hold[rowIndex] = rrow
								hold[ogIndex] = krow
								string = delim.join(hold)
								ogIndex = self.getLastIndex(rows, car)
								if string not in self.boards and string != self.boardString:
									self.boards.append(string)
							else:
								obstacle = True

	def done(self):
		rows = self.boardString.split("|")
		impRow = rows[2]
		bits = list(impRow)
		lastBit = bits[-1]
		if lastBit == "x":
			print(True)
		else:
			print(False)
