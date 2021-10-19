from board import Board
from game import User, AI
X, O = 'X', 'O'

def minimaxAB(board, depth, isMax,alpha, beta):
	#Arreglaré esto xd xd xd xd xd
	if board.isWinner() == 'X': 
		return 10
	elif board.isWinner() == 'O': 
		return -10

	if board.isFilled(depth):
		return 0

	optimal_val = -1000 if isMax else 1000

	for k,v in board._box.items():
		if v == ' ':
			board._box[k] = X if isMax else O
			obtained_val = minimaxAB(board, depth + 1, not isMax, alpha, beta)
			board._box[k] = ' '
			optimal_val = max(optimal_val, obtained_val) if isMax else min(optimal_val, obtained_val)
			if isMax:
				alpha = max(alpha, optimal_val)
			else:
				beta = min(beta, optimal_val)
			if beta <= alpha: 
				break
	return optimal_val
	

def playAI(ai, board):
	optimal_val = ai.optimal_val
	move = -1
	for k,v in board._box.items():
		if v == ' ':
			board._box[k] = X
			obtained_val = minimaxAB(board, 0, ai.isMax, ai.alpha, ai.beta)
			board._box[k] = ' '
			if obtained_val > optimal_val:
				optimal_val = obtained_val
				move = k
	
	board._box[move] = ai.mark

def main():
	print("Tic-Tac-Toe con algoritmo minmax/Poda AlfaBeta")
	mark_decision = input('Seleccione X ó O: ')
	board = Board()
	user = User(mark_decision)
	ai = AI(mark_decision)
	while not board.isFilled(user.turns_counter):
		if not user.turn:
			playAI(ai,board)
			user.turn = not user.turn
		else:
			user.playUser(board)
		board.getBoard()

		if board.isWinner() != '_':
			return print('The winner is: ', board.isWinner())

if __name__ == '__main__':
	main()