from board import Board




def minimaxAB(board, depth, alpha, beta, actual_moves):
	
	if board.isFilled(actual_moves):
		board.getBoard()
	

def main():
	print("Tic-Tac-Toe con algoritmo minmax/Poda AlfaBeta")
	board = Board()
	print(board.print())
	minimaxAB(board, 10, -1000, 1000, 8)


if __name__ == '__main__':
	main()