from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .utils.utils import solve_puzzle
from .utils.board import Board
from .utils.exceptions import BaseOCRException

# Create your views here.

class SolveView(APIView):
    def post(self, request, format=None):
        puzzle = request.data["puzzle"]
        solved_puzzle = solve_puzzle(puzzle)
        if not 1 in solved_puzzle[0]:
            return Response({"puzzle": puzzle, "error": "sudoku not valid"})
        else:
            return Response({"puzzle": puzzle, "solved_puzzle": solved_puzzle})

class OCRView(APIView):
    def post(self, request, format=None):
        board = Board()
        board.prepare_img_from_data(request.data['image'].read())
        board.load_SNN_model("WideResNet")
        try:
            board.ocr_sudoku()
        except BaseOCRException as err:
            return Response({"error": f"{err}"})

        return Response({"puzzle": board.value})
