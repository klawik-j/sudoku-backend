from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from sudoku_ocr import Board

# Create your views here.

class SolveView(APIView):

    # permission_classes = [IsAuthenticated] TBD v1.0.0

    def post(self, request, format=None):
        puzzle = request.data["puzzle"]
        board = Board()
        board.board_value = puzzle
        board.solve()
        error_message = ""
        if not 1 in board.solved_board[0]:
            error_message = "sudoku not valid"
        return Response({
                "solved_puzzle": board.solved_board,
                "error": error_message,
                })

# class OCRView(APIView):

#     # permission_classes = [IsAuthenticated] TBD v1.0.0

#     def post(self, request, format=None):
#         if not 'image' in request.data.keys():
#             return Response({"error": "no image included"})
#         board = Board()
#         board.prepare_img_from_data(request.data['image'].read())
#         board.load_SNN_model("cnn")
#         try:
#             board.ocr_sudoku()
#         except BaseOCRException as err:
#             return Response({
#                 "puzzle": EMPTY_PUZZLE,
#                 "error": f"{err}"})
            
#         return Response({
#             "puzzle": board.value,
#             "error": ""})
