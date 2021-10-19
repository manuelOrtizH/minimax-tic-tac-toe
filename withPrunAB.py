from board import Board
from game import User, AI
X, O = 'X', 'O'

def minimaxAB(board, depth, isMax,alpha, beta):
	#Primera verificación de nuestro método recursivo
	#Encontrar un ganador antes de ejectuar lo demás
	if board.isWinner() == 'X': 
		#En caso de que encontremos un ganador, obtendremos un valor distinto a aquellos que
		#se han considerado óptimos durante la ejecución
		#retornamos los valores que se cuenta inicialmente como maximizador o no
		return 1000
	elif board.isWinner() == 'O': 
		return -1000

	#Verificamos si el tablero está lleno antes de la ejecución
	if board.isFilled(depth):
		return 0
	#Previamente se mencionó como sobre si se consideraba como maximizador o no al jugador
	#Ante esta ejecución, obtenremos los mejores movimientos de tanto el jugador, como la IA
	optimal_val = -1000 if isMax else 1000
	#Recorremos todo el tablero, teniendo un gran árbol de nodos con las diferentes jugadas por hacer
	for k,v in board._box.items():
		if v == ' ':
			#Jugaremos dependiendo si se trata del maximizador o no
			board._box[k] = X if isMax else O
			#Obtenemos una casilla llena, teniendo así un gran árbol que se formará a continuación
			#con nuestro método recursivo
			#Por lo tanto, avanzamos en la profundidad de nuestro gran árbol de nodos
			obtained_val = minimaxAB(board, depth + 1, not isMax, alpha, beta)
			board._box[k] = ' '
			#obtenedremos el valor máximo o mínimo de nuestro valor óptimo, al momento y de nuestro valor obtenido
			#del método recursivo, el cual, en otras palabras, es valor óptimo de la recorrida recursiva que se 
			#obtuvo por esa casillas
			#Es necesario saber si vamos a profundizar o no. En caso de profundizar, necesitamos obtener el valor máximo,
			#necesitamos obtener la mejor forma de no dejarle ganar al usuario
			#de forma contrario, obtenemos la mejor forma de que el usuario no nos prohíba esto
			#hablando como parte de la ia
			optimal_val = max(optimal_val, obtained_val) if isMax else min(optimal_val, obtained_val)
			#al contar con elementos como alpha y beta, los utilizaremos para podar nuestro árbol de nodos
			#*Con nodos, nos referimos a las diferentes opciones que tenemos con nuestro tablero en el juego
			if isMax:
				alpha = max(alpha, optimal_val)
			else:
				beta = min(beta, optimal_val)
			#De la misma forma que es obitene el valor óptimo, es necesario obtener alpha y beta
			#Mientras hacemos backtracking del árbol, 
			#los valores de los nodos se pasarán a los nodos superiores en lugar de los valores alfa y beta,
			#solo pasaremos los valores alfa y beta a los nodos secundarios.
			if alpha >= beta: 
				break
	return optimal_val
	
def playAI(ai, board):
	#Dependiendo del turno que escogió el usuario, la IA utilizará, dependiendo su turno, un valor de infinito
	# infinito = (-1000, 1000)
	#Si juega con las X, querrá decir que no será el maximizador de la partida, al contrario si juega con las O
	#Incializamos variables
	optimal_val = -1000
	move = -1
	#Recorremos el tablero, obteniendo así la jugada más óptima contando con alpha y beta
	for k,v in board._box.items():
		#Encontramos un espacio disponible para jugar
		if v == ' ':
			#Jugamos, para, basarnos en el tablero conforme a esta jugada
			board._box[k] = ai.mark
			#Obtenemos el movimiento óptimo con el algorittmo minmax y alpha y beta
			obtained_val = minimaxAB(board, 0, ai.isMax, ai.alpha, ai.beta)
			#Reseteamos la jugada que se haya ejecutado
			board._box[k] = ' '
			#Basado en el movimiento obtenido y el valor óptimo, comparamos y obtenemos la menor jugada,
			if obtained_val > optimal_val:
				#Si es el caso, actualizamos el valor óptimo para que en siguientes iteraciones, 
				#analizemos sobre esta
				optimal_val = obtained_val
				#El movimiento por hacer en el tablero se actualiza
				move = k
	#La IA hace su jugada en el tablero, después de haber hecho una iteración por los espacios aún vacíos
	#Siendo que, si la IA jugará primero, sería el peor de los casos, al recorrer absoultamente todo el tablero,
	#ya que este se encuentra vacío
	board._box[move] = ai.mark

def main():
	print("Tic-Tac-Toe con algoritmo minmax/Poda AlfaBeta")
	#Tenemos la opción de que el usuario seleccione tanto X como O para jugar
	#Esto afectará en el turno en el que jugará
	mark_decision = input('Seleccione X ó O: ')
	#Se instancian las clases de los diferentes módulos, para obtener diferentes atributos en cada uno.
	board = Board()
	user = User(mark_decision)
	ai = AI(mark_decision)
	#Entraremos a un loop que jugará por turnos hasta que ya no hayan más chances de hacer tu jugada
	while not board.isFilled(user.turns_counter):
		if not user.turn:
			#La IA jugará en caso que el usuario haya tirado ya su jugada
			playAI(ai,board)
			#Después de haceer su jugada, será turno del usuario
			user.turn = not user.turn
		else:
			#Es el turno del usuario y solo se le preguntará por su próxima jugada
			user.play(board)
		#Después de haber hecho una jugada, se imprime el tablero
		board.getBoard()
		#Validación para corroborar que nadie ha ganado aún, si es el caso, terminar juego
		if board.isWinner() != '_':
			return print('The winner is: ', board.isWinner())

if __name__ == '__main__':
	main()