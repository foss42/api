import os
import zipfile
import gdown
from deepface.commons import package_utils, folder_utils
from deepface.models.FacialRecognition import FacialRecognition
from deepface.commons import logger as log

logger = log.get_singletonish_logger()

# --------------------------------
# dependency configuration

tf_major = package_utils.get_tf_major_version()
tf_minor = package_utils.get_tf_minor_version()

if tf_major == 1:
    from keras.models import Model, Sequential
    from keras.layers import (
        Convolution2D,
        MaxPooling2D,
        Flatten,
        Dense,
        Dropout,
    )
else:
    from tensorflow.keras.models import Model, Sequential
    from tensorflow.keras.layers import (
        Convolution2D,
        MaxPooling2D,
        Flatten,
        Dense,
        Dropout,
    )


# -------------------------------------
# pylint: disable=line-too-long, too-few-public-methods
class DeepFaceClient(FacialRecognition):
    """
    Fb's DeepFace model class
    """

    def __init__(self):
        # DeepFace requires tf 2.12 or less
        if tf_major == 2 and tf_minor > 12:
            # Ref: https://github.com/serengil/deepface/pull/1079
            raise ValueError(
                "DeepFace model requires LocallyConnected2D but it is no longer supported"
                f" after tf 2.12 but you have {tf_major}.{tf_minor}. You need to downgrade your tf."
            )

        self.model = load_model()
        self.model_name = "DeepFace"
        self.input_shape = (152, 152)
        self.output_shape = 4096


def load_model(
    url="https://github.com/swghosh/DeepFace/releases/download/weights-vggface2-2d-aligned/VGGFace2_DeepFace_weights_val-0.9034.h5.zip",
) -> Model:
    """
    Construct DeepFace model, download its weights and load
    """
    # we have some checks for this dependency in the init of client
    # putting this in global causes library initialization
    if tf_major == 1:
        from keras.layers import LocallyConnected2D
    else:
        from tensorflow.keras.layers import LocallyConnected2D

    base_model = Sequential()
    base_model.add(
        Convolution2D(32, (11, 11), activation="relu", name="C1", input_shape=(152, 152, 3))
    )
    base_model.add(MaxPooling2D(pool_size=3, strides=2, padding="same", name="M2"))
    base_model.add(Convolution2D(16, (9, 9), activation="relu", name="C3"))
    base_model.add(LocallyConnected2D(16, (9, 9), activation="relu", name="L4"))
    base_model.add(LocallyConnected2D(16, (7, 7), strides=2, activation="relu", name="L5"))
    base_model.add(LocallyConnected2D(16, (5, 5), activation="relu", name="L6"))
    base_model.add(Flatten(name="F0"))
    base_model.add(Dense(4096, activation="relu", name="F7"))
    base_model.add(Dropout(rate=0.5, name="D0"))
    base_model.add(Dense(8631, activation="softmax", name="F8"))

    # ---------------------------------

    home = folder_utils.get_deepface_home()

    if os.path.isfile(home + "/.deepface/weights/VGGFace2_DeepFace_weights_val-0.9034.h5") != True:
        logger.info("VGGFace2_DeepFace_weights_val-0.9034.h5 will be downloaded...")

        output = home + "/.deepface/weights/VGGFace2_DeepFace_weights_val-0.9034.h5.zip"

        gdown.download(url, output, quiet=False)

        # unzip VGGFace2_DeepFace_weights_val-0.9034.h5.zip
        with zipfile.ZipFile(output, "r") as zip_ref:
            zip_ref.extractall(home + "/.deepface/weights/")

    base_model.load_weights(home + "/.deepface/weights/VGGFace2_DeepFace_weights_val-0.9034.h5")

    # drop F8 and D0. F7 is the representation layer.
    deepface_model = Model(inputs=base_model.layers[0].input, outputs=base_model.layers[-3].output)

    return deepface_model
