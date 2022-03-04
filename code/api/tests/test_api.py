from rest_framework.test import APIRequestFactory
from rest_framework.response import Response

from api.views import SolveView

def test_solve_correct_sudoku() -> None:
    request = APIRequestFactory.post(
        '/api/solve/',
        {
            "puzzle": [
            [0, 0, 7, 0, 0, 4, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 1, 5],
            [4, 0, 0, 3, 5, 8, 0, 0, 7],
            [1, 0, 0, 2, 0, 0, 3, 0, 6],
            [0, 5, 0, 0, 3, 0, 0, 7, 2],
            [0, 0, 3, 0, 0, 1, 0, 0, 8],
            [0, 0, 0, 8, 9, 3, 0, 0, 4],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 7, 0, 0, 5, 0, 1]
            ]
        })
    response = SolveView.post(request)
    assert response == Response(
        {
            "solved_puzzle": [
            [5, 6, 7, 1, 2, 4, 8, 3, 9],
            [8, 3, 2, 9, 7, 6, 4, 1, 5],
            [4, 9, 1, 3, 5, 8, 6, 2, 7],
            [1, 4, 9, 2, 8, 7, 3, 5, 6],
            [6, 5, 8, 4, 3, 9, 1, 7, 2],
            [7, 2, 3, 5, 6, 1, 9, 4, 8],
            [2, 1, 5, 8, 9, 3, 7, 6, 4],
            [9, 7, 4, 6, 1, 5, 2, 8, 3],
            [3, 8, 6, 7, 4, 2, 5, 9, 1]
            ],
            "error": ""
        })

def test_solve_incorrect_sudoku() -> None:
    request = APIRequestFactory.post(
        '/api/solve/',
        {
            "puzzle": [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        })
    response = SolveView.post(request)
    assert response == Response(
        {
            "solved_puzzle": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
            "error": "sudoku not valid"
        })