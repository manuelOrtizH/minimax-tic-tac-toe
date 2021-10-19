from board import Board
from game import User, AI
X, O = 'X', 'O'

def minimaxAB(board, depth, isMax,alpha, beta):

	if board.isWinner() == 'X':
		return 10
	elif board.isWinner() == 'O':
		return -10
	else:
		return 0
	
	if isMax:
		optimal_val = -1000
		for k,v in board._box.items():
			if v == ' ':
				board._box[k] = O
				obtained_val = minimaxAB(board, depth + 1, False, alpha, beta)
				optimal_val = max(optimal_val, obtained_val)
				alpha = max(alpha, optimal_val)

				if beta <= alpha: 
					break
		return optimal_val

	else:
		optimal_val = 1000
		for k,v in board._box.items():
			if v == ' ':
				board._box[k] = O
				obtained_val = minimaxAB(board, depth + 1, True, alpha, beta)
				optimal_val = min(optimal_val, obtained_val)
				alpha = min(alpha, optimal_val)

				if beta <= alpha: 
					break
		return optimal_val	


def playAI(ai, board):
	optimal_val = -1000
	move = 0
	for k,v in board._box.items():
		if v == ' ':
			board._box[k] = O
			obtained_val = minimaxAB(board, 0, False, ai.alpha, ai.beta)
			board._box[k] = ' '
			if obtained_val > optimal_val:
				optimal_val = obtained_val
				move = k
	
	board._box[move] = O

def playUser(user, board):
	decision = input('¿En qué casilla desea jugar?: ')
	while not board.isValid(decision):
		print('Esa casilla no es válida.')
		decision = input('¿En qué casilla desea jugar?: ')
	
	board._box[decision] = X
	user.advanceOnGame()

def main():
	print("Tic-Tac-Toe con algoritmo minmax/Poda AlfaBeta")
	board = Board()
	user = User()
	ai = AI()
	while not board.isFilled(user.turns_counter):
		if not user.turn:
			playAI(ai,board)
			user.turn = not user.turn
		else:
			playUser(user, board)
		board.getBoard()

if __name__ == '__main__':
	main()