# First check if theres a winner
# If not, check if there is a tie
# If not, check if there is a move that can be made
'''
Terminal states:
	1. 1 win
	2. -1 loss
	3. 0 tie
'''
# Human player turn
def humanPlayer(self):
	while True:
		try:
			box = int(input("Enter box number: "))
			if box in range(0, 9):
				self.insertSymbol(str(box), 'O')
				return
			else:
				print("Invalid box number")
		except ValueError:
			print("Invalid box number")

# Computer player turn with minimax algorithm
def computerPlayer(self):
	bestScore = -2
	bestMove = 0
	for box in self._box:
		if self._box[box] == ' ':
			self.insertSymbol(str(box), 'X')
			score = minimax(self, 'X')
			self.insertSymbol(str(box), ' ')
			if score > bestScore:
				bestScore = score
				bestMove = box

	self.insertSymbol(str(bestMove), 'X')
	return bestMove


# Minimax algorithm
def minimax(self, player):
	# Check if there is a winner
	if self.isWinner() == 1:
		return 1
	elif self.isWinner() == -1:
		return -1
	# Check if there is a tie
	elif self.checkTie():
		return 0
	# Check if there is a move that can be made
	else:
		# Check if player is computer
		if player == 'X':
			# Find best move
			bestMove = self.minimax(self, 'O')
			return bestMove
		# Check if player is human
		else:
			# Find best move
			bestMove = self.minimax(self, 'X')
			return bestMove

# def computerPlayer(self):
# 	bestScore = -2
# 	bestMove = 0
# 	for box in self._box:
# 		if self.isValid(box):
# 			self.insertSymbol(str(box), X)
# 			score = self.minmax(0, X)
# 			self.insertSymbol(str(box), ' ')
# 			if score > bestScore:
# 				bestScore = score
# 				bestMove = box

#     self.insertSymbol(str(bestMove), X)
# 	return


# def minmax(self, depth, player):
#     if self.isWinner():
#         return 1 if player == X else -1
#     if self.isFilled(depth):
#         return 0
#     scores = []
#     for box in self._box:
#         if self.isValid(box):
#             self.insertSymbol(str(box), player)
#             scores.append(self.minmax(depth + 1, O if player == X else X))
#             self.insertSymbol(str(box), ' ')
#     if player == X:
#         return max(scores)
#     else:
#         return min(scores)    

# if __name__ == '__main__':
# 	print('Moni')
