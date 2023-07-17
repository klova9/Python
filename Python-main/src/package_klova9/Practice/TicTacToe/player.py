import math 
import random as ran
class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        empty_square = False
        val = None
        while not empty_square: 
            square = input(self.letter + '\'s turn.')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                empty_square = True
            except ValueError:
                print('No square')
                
class CPUPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = ran.choice(game.available_moves())
        return super().get_move(game)

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn\nInput move (0-9)')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('No square')
        return val