from typing import List
from pathlib import Path
from math import sqrt

from imutils.perspective import four_point_transform
from imutils import grab_contours, resize
from skimage.segmentation import clear_border
from numpy import array, ndarray, expand_dims, fromstring, uint8
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2

from .image import Image
from .exceptions import NotProperOCR, SudokuBoardNotFound


class Board:
    """Class of a sudoku board."""

    MNIST_MODELS = {
        "WideResNet": Path("/code/api/utils/WideResNet28_10.h5"),
    }

    def prepare_img_from_path(self, img_path: Path) -> None:
        """Load board img from path.

        Args:
            img_path (Path): path to board img
        Raises:
            err: Image have not been found
        """
        self._data = cv2.imread(img_path)
        if self._data is None:
            raise OSError(f"file {img_path} not found")
        self.resize_img = resize(self.original_img, width=600)

    def prepare_img_from_data(self, img_file: bytes) -> None:
        """Load board image from file.

        Args:
            img_file (ndarray): img data
        """
        self.original_img = cv2.imdecode(fromstring(img_file, uint8), cv2.IMREAD_UNCHANGED)
        self.resize_img = resize(self.original_img, width=600)

    def load_SNN_model(self, model_name: str) -> None:
        """Load SNN model.

        Args:
            model_name (str): name of SNN model

        Raises:
            err: SNN model file have not been found
        """
        try:
            self.model = load_model(self.MNIST_MODELS[model_name])
        except OSError as err:
            raise err(f"MNIST model not fund in directory: {self.MNIST_MODEL_PATH}")

    def ocr_sudoku(self) -> None:
        """OCR sudoku."""
        if not self.original_img.any():
            raise ValueError("image not loaded")

        self.image_thresh = self._thresholding_image(self.resize_img)
        self.board_contours = self._find_board_contour(
            self._find_contours(self.image_thresh),
        )
        self.board = self._adjust_perspective(
            self.resize_img,
            self.board_contours,
        )
        self.cells_cords = self._find_cells(self.board)
        self._value = self._board_img_to_value()
        if not self._value.any():
            raise NotProperOCR("No digits found")

    @property
    def value(self):
        """Return _value."""
        return self._value

    def _board_img_to_value(self) -> array:
        """Return board represetation as array from img."""
        value = []
        for cell_cords in self.cells_cords:
            cell = self.board[
                cell_cords[2] : cell_cords[3],
                cell_cords[0] : cell_cords[1],
            ]
            improved_cell = self._cell_image_impovement(cell)
            if not self._cell_is_empty(improved_cell):
                digit = self._find_digit(improved_cell)
                if digit == 0:
                    digit = 8
                value.append(digit)
            else:
                value.append(0)
        board_size = int(sqrt(len(value)))
        value = array(value)
        return value.reshape(board_size, board_size)

    @staticmethod
    def _thresholding_image(img: ndarray) -> ndarray:
        """Apply thresholding_image on image.

        Args:
            img (ndarray): image

        Returns:
            ndarray: treshold of image
        """
        grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(grayscale, (7, 7), 3)
        thresh = cv2.adaptiveThreshold(
            blurred,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2,
        )
        inverse = cv2.bitwise_not(thresh)
        return inverse

    @staticmethod
    def _find_contours(img: ndarray) -> ndarray:
        """Find contours.

        Args:
            img (ndarray): image

        Returns:
            ndarray: all contours in image
        """
        contours = cv2.findContours(
            img,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )
        contours = grab_contours(contours)
        return sorted(contours, key=cv2.contourArea, reverse=True)

    @staticmethod
    def _find_board_contour(contours: ndarray) -> ndarray:
        """Look for contours of sudoku board.

        Args:
            contours (ndarray): all contours in image

        Raises:
            Exception: contours in image are not sudoku board

        Returns:
            ndarray: sudoku board contours
        """
        const = 0.02
        for cnt in contours:
            approx = cv2.approxPolyDP(
                cnt,
                const * cv2.arcLength(cnt, True),
                True,
            )
            if len(approx) == 4:
                return approx
        raise SudokuBoardNotFound("Sudoku board not found")

    @staticmethod
    def _adjust_perspective(img: ndarray, board_contours: ndarray) -> ndarray:
        """Adjust perspective.

        Use four point transformation

        Args:
            img (ndarray): image
            board_contours (ndarray): contours fo board

        Returns:
            ndarray: image of board and nothing else
        """
        board = four_point_transform(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), board_contours.reshape(4, 2))
        return board

    @staticmethod
    def _find_cells(board: ndarray) -> List:
        """Look for cells coordinates.

        Args:
            board (ndarray): image of board

        Returns:
            List: list of coordinates

        +---+---+---+---+---+---+---+---+---+
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        +---+---+---+---+---+---+---+---+---+
        | 9 | 10| 11| 12| 13| 14| 15| 16| 17|
        +---+---+---+---+---+---+---+---+---+

        .
        .
        .
        +---+---+---+---+---+---+---+---+---+
        | 80| 81| 82| 83| 84| 85| 86| 87| 88|
        +---+---+---+---+---+---+---+---+---+
        """
        cell_width = board.shape[1] // 9
        cell_height = board.shape[0] // 9

        cells_cords = []

        for y in range(0, 9):
            for x in range(0, 9):
                cell_x_start = x * cell_width
                cell_x_end = (x + 1) * cell_width
                cell_y_start = y * cell_height
                cell_y_end = (y + 1) * cell_height

                cell = (cell_x_start, cell_x_end, cell_y_start, cell_y_end)
                cells_cords.append(cell)

        return cells_cords

    @staticmethod
    def _cell_image_impovement(cell: ndarray) -> ndarray:
        """Improve cell's img."""
        # blurred = cv2.GaussianBlur(cell, (7, 7), 1)
        thresh = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = clear_border(thresh)

        return thresh

    @staticmethod
    def _cell_is_empty(cell: ndarray) -> bool:
        """Determine if cell is empty or not."""
        mask = cv2.inRange(cell, 254, 255)
        height, width = mask.shape[:2]
        number_of_pixels = height * width
        count_white = cv2.countNonZero(mask)
        percent_white = count_white * 100 / number_of_pixels

        if percent_white < 5:
            return True
        else:
            return False

    def _find_digit(self, cell: ndarray) -> int:
        """Recognise digit on img."""
        cell_ = cv2.resize(cell, (28, 28))
        cell_ = cell_.astype("float") / 255.0
        cell_ = img_to_array(cell_)
        cell_ = expand_dims(cell_, axis=0)
        prediction = self.model.predict(cell_).argmax(axis=1)[0]

        return prediction
