def print_sudoku(board):
    print("+" + "---+"*9)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("-" + "----"*9)
        else:
            print("+" + "   +"*9)
