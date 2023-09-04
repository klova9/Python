import random as ran
import regex as re

# TODO : build GUI using Tkinter

class Board:
    def __init__(self, board_size, bomb_count):
        self.board_size = board_size
        self.bomb_count = bomb_count
        self.board = self.new_board()
        self.assign_values_to_board()
        self.dug = set()
        

    def new_board(self):
        board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        hidden_bomb = 0
        while hidden_bomb < self.bomb_count:
            bomb_location = ran.randint(0, self.board_size**2-1)
            row = bomb_location // self.board_size
            column = bomb_location % self.board_size
            if board[row][column] == '*':
                continue
            board[row][column] = '*'
            hidden_bomb += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.board_size):
            for c in range(self.board_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.num_neighboring_bombs(r, c)

    def num_neighboring_bombs(self, row, column):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.board_size - 1, row+1)+1):
            for c in range(max(0, column-1), min(self.board_size - 1, column+1)+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

    def dig(self, row, column):
        self.dug.add(row, column)
        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True
        for r in range(max(0, row-1), min(self.board_size - 1, row+1)+1):
            for c in range(max(0, column-1), min(self.board_size - 1, column+1)+1):
                if (r, c) in self.dig:
                    continue
            self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(
            self.board_size)] for _ in range(self.board_size)]
        for row in range(self.board_size):
            for column in range(self.board_size):
                if (row, column) in self.dug:
                    visible_board[row][column] = str(self.board[row][column])
                else:
                    visible_board[row][column] = ''

        string_rep = ''
        widths = []
        for idx in range(self.board_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.board_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.board_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
def play(board_size=10, bomb_count=10):
    board = Board(board_size, bomb_count)
    safe = True
    while len(board.dug) < board.board_size ** 2 - bomb_count:
        print(board)
        user_input = re.split(',(\\s)*', input('Enter coordinate to dig: '))
        row, column = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.board_size or column < 0 or column >= board.board_size:
            print('Invalid coordinate!\nEnter valid coordinate(row,column): ')
            continue
        safe = board.dig(row, column)
        if not safe:
            print('You\'ve hit a bomb!')
            break
    if safe:
        print('You cleared the minefield!')
    else:
        print('You\'ve lost!\nHopefully your replacement will succed where you failed!')
        board.dug = [(r,c) for r in range(board.board_size) for c in range(board.board_size)]
        print(board)
        
if __name__ == '__main__':
    play()