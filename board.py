from withoutPrun import *

CHECK_BOXES = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
X, O = 'X', 'O'

class Board:
    def __init__(self):
        #Usaremos un diccionario para representar el tablero y de esta forma, sea más eficiente la búsqueda
        self._box = {}
        self.max_movements = 9
        #Generamos los espacios en blanco, con su correspondiente llave representando la casilla
        for i, check_box in enumerate(CHECK_BOXES):
            self._box[str(i)] = check_box
    
    def getBoard(self):
        #Impresión del tablero en la terminal
        print(f'''  
        {self._box['0']} | {self._box['1']} | {self._box['2']}
        _________   
        {self._box['3']} | {self._box['4']} | {self._box['5']}
        _________
        {self._box['6']} | {self._box['7']} | {self._box['8']}
        ''')

    def isValid(self, space_box):
        #Se valida si el movimiento a realizar en la casilla no ocupa ya un movimiento hecho
        return False if self._box[space_box] != ' ' else True

    def isFilled(self, actual_movements):
        #Se verifica que el tablero esté lleno o no
        return False if self.max_movements > actual_movements else True

    def isWinner(self):
        if self._box['0'] == self._box['1'] == self._box['2'] != ' ':
            return True
        elif self._box['3'] == self._box['4'] == self._box['5'] != ' ':
            return True
        elif self._box['6'] == self._box['7'] == self._box['8'] != ' ':
            return True
        elif self._box['0'] == self._box['3'] == self._box['6'] != ' ':
            return True
        elif self._box['1'] == self._box['4'] == self._box['7'] != ' ':
            return True
        elif self._box['2'] == self._box['5'] == self._box['8'] != ' ':
            return True
        elif self._box['0'] == self._box['4'] == self._box['8'] != ' ':
            return True
        elif self._box['2'] == self._box['4'] == self._box['6'] != ' ':
            return True
        else:
            return False 

    #Método para insertar simbolo en casilla
    def insertSymbol(self, space_box, player):
        if self.isValid(space_box):
            self._box[space_box] = player
            self.max_movements -= 1
            self.getBoard()
        else:
            print('Movimiento inválido')

    def checkTie(self):
        if self.isFilled(self.max_movements):
            print('Empate')
            return True
        else:
            return False
    

if __name__ == '__main__':
    board = Board()
    board.getBoard()
    # Human player gets O
    humanPlayer(board)
    # Computer player gets X
    computerPlayer(board)



    


