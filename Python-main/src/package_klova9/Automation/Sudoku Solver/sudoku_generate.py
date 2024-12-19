def generate_sudoku():
    """
    Generates a sudoku puzzle with a unique solution.
    """
    # Generate a random filled-in sudoku board
    board = generate_full_board()
    # Remove numbers from the board to create a puzzle
    puzzle = remove_numbers(board)
    return puzzle

def generate_full_board():
    """
    Generates a random filled-in sudoku board.
    """
    # Create an empty 9x9 board
    board = [[-1 for _ in range(9)] for _ in range(9)]
    # Fill the board with a valid sudoku solution
    solve_sudoku(board)
    return board