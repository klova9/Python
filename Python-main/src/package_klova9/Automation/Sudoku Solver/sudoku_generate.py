from random import randint as random
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

def remove_numbers(board):
    """
    Removes numbers from the board to create a sudoku puzzle.
    """
    # Create a list of all the cells in the board
    cells = [(row, col) for row in range(9) for col in range(9)]
    # Shuffle the list of cells
    random.shuffle(cells)
    # Create a copy of the board
    puzzle = copy.deepcopy(board)
    # Remove numbers from the board until there is only one solution
    for row, col in cells:
        # Save the current value of the cell
        value = puzzle[row][col]
        # Remove the value from the cell
        puzzle[row][col] = -1
        # Check if the board has a unique solution
        if not has_unique_solution(puzzle):
            # If the board does not have a unique solution, restore the value
            puzzle[row][col] = value
    return puzzle