from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import numpy as np

# Notice that all facial detector models must be inherited from this class


# pylint: disable=unnecessary-pass, too-few-public-methods
class Detector(ABC):
    @abstractmethod
    def detect_faces(self, img: np.ndarray) -> List["FacialAreaRegion"]:
        """
        Interface for detect and align face

        Args:
            img (np.ndarray): pre-loaded image as numpy array

        Returns:
            results (List[FacialAreaRegion]): A list of FacialAreaRegion objects
                where each object contains:

            - facial_area (FacialAreaRegion): The facial area region represented
                as x, y, w, h, left_eye and right_eye. left eye and right eye are
                eyes on the left and right respectively with respect to the person
                instead of observer.
        """
        pass


class FacialAreaRegion:
    x: int
    y: int
    w: int
    h: int
    left_eye: Tuple[int, int]
    right_eye: Tuple[int, int]
    confidence: float

    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        left_eye: Optional[Tuple[int, int]] = None,
        right_eye: Optional[Tuple[int, int]] = None,
        confidence: Optional[float] = None,
    ):
        """
        Initialize a Face object.

        Args:
            x (int): The x-coordinate of the top-left corner of the bounding box.
            y (int): The y-coordinate of the top-left corner of the bounding box.
            w (int): The width of the bounding box.
            h (int): The height of the bounding box.
            left_eye (tuple): The coordinates (x, y) of the left eye with respect to
                the person instead of observer. Default is None.
            right_eye (tuple): The coordinates (x, y) of the right eye with respect to
                the person instead of observer. Default is None.
            confidence (float, optional): Confidence score associated with the face detection.
                Default is None.
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.confidence = confidence


class DetectedFace:
    img: np.ndarray
    facial_area: FacialAreaRegion
    confidence: float

    def __init__(self, img: np.ndarray, facial_area: FacialAreaRegion, confidence: float):
        """
        Initialize detected face object.

        Args:
            img (np.ndarray): detected face image as numpy array
            facial_area (FacialAreaRegion): detected face's metadata (e.g. bounding box)
            confidence (float): confidence score for face detection
        """
        self.img = img
        self.facial_area = facial_area
        self.confidence = confidence
