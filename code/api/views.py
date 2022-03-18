from typing import Any

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from sudoku_ocr import Board

from api.serializers import OcrViewSerializer, SolveViewSerializer


class SolveViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for api/solve."""

    permission_classes = [IsAuthenticated]
    serializer_class = SolveViewSerializer

    def create(self, request: Any) -> Response:
        """Overwite create method to return Response instead of query db."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        board = Board()
        board.board_value = serializer.data["puzzle"]
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

    def get_queryset(self) -> None:
        """Overwrite qet_queryset method to pass instead of return queryset."""
        pass


class OcrViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for api/ocr."""

    permission_classes = [IsAuthenticated]
    serializer_class = OcrViewSerializer

    def create(self, request: Any) -> Response:
        """Overwite create method to return Response instead of query db."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        board = Board()
        board.prepare_img_from_data(request.data["puzzle_image"].read())
        board.ocr_sudoku()

        return Response(
            {"puzzle": board.board_value, "error": ""},
        )

    def get_queryset(self) -> None:
        """Overwrite qet_queryset method to pass instead of return queryset."""
        pass
