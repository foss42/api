# built-in dependencies
from typing import Any, Dict, List, Union

# 3rd party dependencies
import numpy as np

# project dependencies
from deepface.commons import image_utils
from deepface.modules import modeling, detection, preprocessing
from deepface.models.FacialRecognition import FacialRecognition


def represent(
    img_path: Union[str, np.ndarray],
    model_name: str = "VGG-Face",
    enforce_detection: bool = True,
    detector_backend: str = "opencv",
    align: bool = True,
    expand_percentage: int = 0,
    normalization: str = "base",
) -> List[Dict[str, Any]]:
    """
    Represent facial images as multi-dimensional vector embeddings.

    Args:
        img_path (str or np.ndarray): The exact path to the image, a numpy array in BGR format,
            or a base64 encoded image. If the source image contains multiple faces, the result will
            include information for each detected face.

        model_name (str): Model for face recognition. Options: VGG-Face, Facenet, Facenet512,
            OpenFace, DeepFace, DeepID, Dlib, ArcFace, SFace and GhostFaceNet

        enforce_detection (boolean): If no face is detected in an image, raise an exception.
            Default is True. Set to False to avoid the exception for low-resolution images.

        detector_backend (string): face detector backend. Options: 'opencv', 'retinaface',
            'mtcnn', 'ssd', 'dlib', 'mediapipe', 'yolov8', 'centerface' or 'skip'.

        align (boolean): Perform alignment based on the eye positions.

        expand_percentage (int): expand detected facial area with a percentage (default is 0).

        normalization (string): Normalize the input image before feeding it to the model.
            Default is base. Options: base, raw, Facenet, Facenet2018, VGGFace, VGGFace2, ArcFace

    Returns:
        results (List[Dict[str, Any]]): A list of dictionaries, each containing the
            following fields:

        - embedding (List[float]): Multidimensional vector representing facial features.
            The number of dimensions varies based on the reference model
            (e.g., FaceNet returns 128 dimensions, VGG-Face returns 4096 dimensions).
        - facial_area (dict): Detected facial area by face detection in dictionary format.
            Contains 'x' and 'y' as the left-corner point, and 'w' and 'h'
            as the width and height. If `detector_backend` is set to 'skip', it represents
            the full image area and is nonsensical.
        - face_confidence (float): Confidence score of face detection. If `detector_backend` is set
            to 'skip', the confidence will be 0 and is nonsensical.
    """
    resp_objs = []

    model: FacialRecognition = modeling.build_model(model_name)

    # ---------------------------------
    # we have run pre-process in verification. so, this can be skipped if it is coming from verify.
    target_size = model.input_shape
    if detector_backend != "skip":
        img_objs = detection.extract_faces(
            img_path=img_path,
            detector_backend=detector_backend,
            grayscale=False,
            enforce_detection=enforce_detection,
            align=align,
            expand_percentage=expand_percentage,
        )
    else:  # skip
        # Try load. If load error, will raise exception internal
        img, _ = image_utils.load_image(img_path)

        if len(img.shape) != 3:
            raise ValueError(f"Input img must be 3 dimensional but it is {img.shape}")

        # make dummy region and confidence to keep compatibility with `extract_faces`
        img_objs = [
            {
                "face": img,
                "facial_area": {"x": 0, "y": 0, "w": img.shape[0], "h": img.shape[1]},
                "confidence": 0,
            }
        ]
    # ---------------------------------

    for img_obj in img_objs:
        img = img_obj["face"]

        # rgb to bgr
        img = img[:, :, ::-1]

        region = img_obj["facial_area"]
        confidence = img_obj["confidence"]

        # resize to expected shape of ml model
        img = preprocessing.resize_image(
            img=img,
            # thanks to DeepId (!)
            target_size=(target_size[1], target_size[0]),
        )

        # custom normalization
        img = preprocessing.normalize_input(img=img, normalization=normalization)

        embedding = model.forward(img)

        resp_obj = {}
        resp_obj["embedding"] = embedding
        resp_obj["facial_area"] = region
        resp_obj["face_confidence"] = confidence
        resp_objs.append(resp_obj)

    return resp_objs
