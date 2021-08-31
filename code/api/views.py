from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .utils.utils import build_board, solve_puzzle

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
        data  = request.data
        print(type(data["image"]))

        return Response({"poszlo": "tak"})
