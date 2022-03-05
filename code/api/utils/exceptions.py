class BaseOCRException(Exception):
    """Base class for exceptions related to OCR process."""

    pass


class SudokuBoardNotFound(BaseOCRException):
    """Raise when sudoku board's similar object have not been found in image."""

    pass


class NotProperOCR(BaseOCRException):
    """Raise when not found any digits in sudoku board."""

    pass
