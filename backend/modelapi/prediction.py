import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

class Predict:
    model_filename = 'glaucoma.h5'
    model_path = os.path.join(os.path.dirname(__file__), '..', model_filename)

    def __init__(self):
        print("Prediction model initialization")

    def prediction(self, input_data):
        try:
            # Load the model
            model = tf.keras.models.load_model(self.model_path)
            print("Model loaded successfully from:", self.model_path)

            # Make predictions using the loaded model
            input_data_resized = image.array_to_img(input_data.resize((240, 240)))
            input_data_array = image.img_to_array(input_data_resized)
            input_data_array = np.expand_dims(input_data_array, axis=0)
            predictions = model.predict(input_data_array)

            if predictions[0][0] != 1:
                return "Glaucoma"
            else:
                return "Normal"

        except Exception as e:
            print(e)
