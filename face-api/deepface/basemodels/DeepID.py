import os
import gdown
from deepface.commons import package_utils, folder_utils
from deepface.models.FacialRecognition import FacialRecognition
from deepface.commons import logger as log

logger = log.get_singletonish_logger()

tf_version = package_utils.get_tf_major_version()

if tf_version == 1:
    from keras.models import Model
    from keras.layers import (
        Conv2D,
        Activation,
        Input,
        Add,
        MaxPooling2D,
        Flatten,
        Dense,
        Dropout,
    )
else:
    from tensorflow.keras.models import Model
    from tensorflow.keras.layers import (
        Conv2D,
        Activation,
        Input,
        Add,
        MaxPooling2D,
        Flatten,
        Dense,
        Dropout,
    )

# pylint: disable=line-too-long


# -------------------------------------

# pylint: disable=too-few-public-methods
class DeepIdClient(FacialRecognition):
    """
    DeepId model class
    """

    def __init__(self):
        self.model = load_model()
        self.model_name = "DeepId"
        self.input_shape = (47, 55)
        self.output_shape = 160


def load_model(
    url="https://github.com/serengil/deepface_models/releases/download/v1.0/deepid_keras_weights.h5",
) -> Model:
    """
    Construct DeepId model, download its weights and load
    """

    myInput = Input(shape=(55, 47, 3))

    x = Conv2D(20, (4, 4), name="Conv1", activation="relu", input_shape=(55, 47, 3))(myInput)
    x = MaxPooling2D(pool_size=2, strides=2, name="Pool1")(x)
    x = Dropout(rate=0.99, name="D1")(x)

    x = Conv2D(40, (3, 3), name="Conv2", activation="relu")(x)
    x = MaxPooling2D(pool_size=2, strides=2, name="Pool2")(x)
    x = Dropout(rate=0.99, name="D2")(x)

    x = Conv2D(60, (3, 3), name="Conv3", activation="relu")(x)
    x = MaxPooling2D(pool_size=2, strides=2, name="Pool3")(x)
    x = Dropout(rate=0.99, name="D3")(x)

    x1 = Flatten()(x)
    fc11 = Dense(160, name="fc11")(x1)

    x2 = Conv2D(80, (2, 2), name="Conv4", activation="relu")(x)
    x2 = Flatten()(x2)
    fc12 = Dense(160, name="fc12")(x2)

    y = Add()([fc11, fc12])
    y = Activation("relu", name="deepid")(y)

    model = Model(inputs=[myInput], outputs=y)

    # ---------------------------------

    home = folder_utils.get_deepface_home()

    if os.path.isfile(home + "/.deepface/weights/deepid_keras_weights.h5") != True:
        logger.info("deepid_keras_weights.h5 will be downloaded...")

        output = home + "/.deepface/weights/deepid_keras_weights.h5"
        gdown.download(url, output, quiet=False)

    model.load_weights(home + "/.deepface/weights/deepid_keras_weights.h5")

    return model
