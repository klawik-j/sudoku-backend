from sudoku import Sudoku

def build_board(
    A1, A2, A3, A4, A5, A6, A7, A8, A9,
    B1, B2, B3, B4, B5, B6, B7, B8, B9,
    C1, C2, C3, C4, C5, C6, C7, C8, C9,
    D1, D2, D3, D4, D5, D6, D7, D8, D9,
    E1, E2, E3, E4, E5, E6, E7, E8, E9,
    F1, F2, F3, F4, F5, F6, F7, F8, F9,
    G1, G2, G3, G4, G5, G6, G7, G8, G9,
    H1, H2, H3, H4, H5, H6, H7, H8, H9,
    I1, I2, I3, I4, I5, I6, I7, I8, I9,
):
    return [
        [int(A1), int(A2), int(A3), int(A4), int(A5), int(A6), int(A7), int(A8), int(A9),],
        [int(B1), int(B2), int(B3), int(B4), int(B5), int(B6), int(B7), int(B8), int(B9),],
        [int(C1), int(C2), int(C3), int(C4), int(C5), int(C6), int(C7), int(C8), int(C9),],
        [int(D1), int(D2), int(D3), int(D4), int(D5), int(D6), int(D7), int(D8), int(D9),],
        [int(E1), int(E2), int(E3), int(E4), int(E5), int(E6), int(E7), int(E8), int(E9),],
        [int(F1), int(F2), int(F3), int(F4), int(F5), int(F6), int(F7), int(F8), int(F9),],
        [int(G1), int(G2), int(G3), int(G4), int(G5), int(G6), int(G7), int(G8), int(G9),],
        [int(H1), int(H2), int(H3), int(H4), int(H5), int(H6), int(H7), int(H8), int(H9),],
        [int(I1), int(I2), int(I3), int(I4), int(I5), int(I6), int(I7), int(I8), int(I9),],
    ]

def solve_puzzle(board):
    puzzle = Sudoku(3, 3, board=board)
    return puzzle.solve().board