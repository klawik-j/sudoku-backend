from django.http import JsonResponse, HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils.utils import solve_puzzle, EMPTY_PUZZLE
from .utils.board import Board
from .utils.exceptions import BaseOCRException

# Create your views here.

class SolveView(APIView):

    # permission_classes = [IsAuthenticated] TBD v1.0.0

    def post(self, request, format=None):
        puzzle = request.data["puzzle"]
        solved_puzzle = solve_puzzle(puzzle)
        if not 1 in solved_puzzle[0]:
            return Response({
                "solved_puzzle": EMPTY_PUZZLE,
                "error": "sudoku not valid",
                })
        else:
            return Response({
                "solved_puzzle": solved_puzzle,
                "error": ""})

class OCRView(APIView):

    # permission_classes = [IsAuthenticated] TBD v1.0.0

    def post(self, request, format=None):
        if not 'image' in request.data.keys():
            return Response({"error": "no image included"})
        board = Board()
        board.prepare_img_from_data(request.data['image'].read())
        board.load_SNN_model("cnn")
        try:
            board.ocr_sudoku()
        except BaseOCRException as err:
            return Response({
                "puzzle": EMPTY_PUZZLE,
                "error": f"{err}"})
            
        return Response({
            "puzzle": board.value,
            "error": ""})
