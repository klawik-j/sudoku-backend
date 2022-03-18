from typing import Any

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from sudoku_ocr import Board

from api.serializers import OcrViewSerializer

# Create your views here.


class SolveView(APIView):
    """Solve view class."""

    permission_classes = [IsAuthenticated]

    def post(self, request: Any) -> Response:
        """Post method for Solve view."""
        puzzle = request.data["puzzle"]
        board = Board()
        board.board_value = puzzle
        board.solve()
        error_message = ""
        if 1 not in board.solved_board[0]:
            error_message = "sudoku not valid"
        return Response(
            {
                "solved_puzzle": board.solved_board,
                "error": error_message,
            }
        )


class OcrViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for api/ocr."""

    permission_classes = [IsAuthenticated]
    serializer_class = OcrViewSerializer

    def create(self, request: Any) -> Response:
        """Overwite create method to return Response instead of query db."""
        board = Board()
        board.prepare_img_from_data(request.data["puzzle_image"].read())
        board.ocr_sudoku()

        return Response(
            {"puzzle": board.board_value, "error": ""},
        )

    def get_queryset(self) -> None:
        """Overwrite qet_queryset method to pass instead of return queryset."""
        pass
