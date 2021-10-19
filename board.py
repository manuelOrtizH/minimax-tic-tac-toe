CHECK_BOXES = [' ', ' ', ' ', 
               ' ', ' ', ' ', 
               ' ', ' ', ' ']
X, O = 'X', 'O'

class Board:
    def __init__(self):
        #Usaremos un diccionario para representar el tablero y de esta forma, sea más eficiente la búsqueda
        self._box = {}
        self.max_movements = 5
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
        #Diagonal
        if self._box['0'] == X and self._box['4'] == X and self._box['8'] == X:
            return X
        elif self._box['2'] == X and self._box['4'] == X and self._box['6'] == X:
            return X
        #Horizontal 
        elif self._box['0'] == X and self._box['1'] == X and self._box['2'] == X:
            return X
        elif self._box['3'] == X and self._box['4'] == X and self._box['5'] == X:
            return X
        elif self._box['6'] == X and self._box['7'] == X and self._box['8'] == X:
            return X
        #Vertical
        elif self._box['0'] == X and self._box['3'] == X and self._box['6'] == X:
            return X
        elif self._box['1'] == X and self._box['4'] == X and self._box['7'] == X:
            return X
        elif self._box['2'] == X and self._box['5'] == X and self._box['8'] == X:
            return X
        #Diagonal
        elif self._box['0'] == O and self._box['4'] == O and self._box['8'] == O:
            return O
        elif self._box['2'] == O and self._box['4'] == O and self._box['6'] == O:
            return O
        #Horizontal 
        elif self._box['0'] == O and self._box['1'] == O and self._box['2'] == O:
            return O
        elif self._box['3'] == O and self._box['4'] == O and self._box['5'] == O:
            return O
        elif self._box['6'] == O and self._box['7'] == O and self._box['8'] == O:
            return O
        #Vertical
        elif self._box['0'] == O and self._box['3'] == O and self._box['6'] == O:
            return O
        elif self._box['1'] == O and self._box['4'] == O and self._box['7'] == O:
            return O
        elif self._box['2'] == O and self._box['5'] == O and self._box['8'] == O:
            return O
        else:
            return '_'
    

    #Método para insertar simbolo en casilla
    def insertSymbol(self, space_box, player):
        self._box[space_box] = player
        self.max_movements -= 1

if __name__ == '__main__':
    board = Board()
    board.getBoard()
    board.insertSymbol('0', 'X')
    board.getBoard()    