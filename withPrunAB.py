from board import Board
X, O = 'X', 'O'
isYourTurn = True

class Player:
	def __init__(self):
		self.turn = False
		self.remaining_turns = 0

	def advanceOnGame(self):
		self.remaining_turns+=1
		self.turn = not self.turn

def minimaxAB(board, player, alpha, beta):
	
	#Validació inicial de recursión
	if board.isFilled(player.remaining_turns):
		return board

def main():
	print("Tic-Tac-Toe con algoritmo minmax/Poda AlfaBeta")
	board = Board()
	player = Player()
	best_play = minimaxAB(board, player, -1000, 1000)
	print(best_play)

if __name__ == '__main__':
	main()