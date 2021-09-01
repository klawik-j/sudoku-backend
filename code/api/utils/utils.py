from sudoku import Sudoku

def solve_puzzle(board):
    puzzle = Sudoku(3, 3, board=board)
    return puzzle.solve().board