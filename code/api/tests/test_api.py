def test_solve_correct_sudoku() -> None:
    """Test post /api/solve with correct sudoku in data."""
    pass


def test_solve_incorrect_sudoku() -> None:
    """Test post /api/solve with incorrect sudoku in data."""
    pass


# class SolveTests(APITestCase):
#     def test_solve_correct_sudoku(self) -> None:
#         #url = reverse('solve')
#         data = {
#                 "puzzle": [
#                 [0, 0, 7, 0, 0, 4, 0, 0, 9],
#                 [0, 0, 0, 0, 0, 0, 0, 1, 5],
#                 [4, 0, 0, 3, 5, 8, 0, 0, 7],
#                 [1, 0, 0, 2, 0, 0, 3, 0, 6],
#                 [0, 5, 0, 0, 3, 0, 0, 7, 2],
#                 [0, 0, 3, 0, 0, 1, 0, 0, 8],
#                 [0, 0, 0, 8, 9, 3, 0, 0, 4],
#                 [0, 7, 0, 0, 0, 0, 0, 0, 3],
#                 [3, 0, 0, 7, 0, 0, 5, 0, 1]
#                 ]
#             }
#         # response = self.client.post(url, data, format='json')
#         # print(response)
#         pass

# def test_solve_incorrect_sudoku() -> None:
#     request = APIRequestFactory.post(
#         '/api/solve/',
#         {
#             "puzzle": [
#             [1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0]
#             ]
#         })
#     response = SolveView.post(request)
#     assert response == Response(
#         {
#             "solved_puzzle": [
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         ],
#             "error": "sudoku not valid"
#         })
