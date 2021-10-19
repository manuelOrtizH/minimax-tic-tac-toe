class Player:
	def __init__(self):
		self.actual_movement = 0
		self.prev_movement = 0
		self.turns_counter = 0

class User(Player):
	def __init__(self):
		self.turn = True
		super().__init__()

	def advanceOnGame(self):
		self.turns_counter+=1
		self.turn = not self.turn

class AI(Player):
	def __init__(self):
		self.best_movement = 0
		self.alpha = -1000
		self.beta = 1000
		super().__init__()