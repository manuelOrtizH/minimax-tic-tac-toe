X, O = 'X', 'O'
class Player:
    def __init__(self, mark):
        self.actual_movement = 0
        self.prev_movement = 0
        self.turns_counter = 0
        self.mark = mark

class User(Player):
    def __init__(self, mark):
        self.turn = False if mark == O else True
        super().__init__(mark)

    def advanceOnGame(self):
        self.turns_counter+=1
        self.turn = not self.turn

    def playUser(self, board):
        decision = input('¿En qué casilla desea jugar?: ')
        while not board.isValid(decision):
            print('Esa casilla no es válida.')
            decision = input('¿En qué casilla desea jugar?: ')
        
        board._box[decision] = self.mark
        self.advanceOnGame()

class AI(Player):
    def __init__(self, user_mark):
        self.alpha = -1000
        self.beta = 1000
        self.optimal_val = -1000 
        self.isMax = True
        super().__init__(X if user_mark == O else O)
        if self.mark == X:
            self.isMax = False
    
        
