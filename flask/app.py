import os
import numpy as np
import pickle
# Tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Load Labels
labels = pickle.load(open('labels.pkl','rb'))

# Model saved with Keras model.save()
MODEL_PATH ='best_weights.h5'

# Load your trained model
model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    ## Scaling
    x = x/255
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    preds_idx = np.argmax(preds, axis=1)
    if preds_idx==0:
        preds_idx="The leaf is healthy"
    elif preds_idx==1:
        preds_idx="The leaf has Multiple Disease"
    elif preds_idx==2:
        preds_idx="The leaf is infected with Rust"
    else:
        preds_idx="The leaf has Scab"
        
    return preds_idx


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        print(preds)
        return preds
    return None


if __name__ == '__main__':
    app.run(debug=True)
