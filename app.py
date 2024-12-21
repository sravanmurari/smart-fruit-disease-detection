from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import json
import os
from pesticides import get_pesticide_recommendations  

app = Flask(__name__)

# Load the model
model = load_model('models/fruit_disease_classifier.keras')

# Load class indices
with open('models/class_indices.json') as f:
    class_indices = json.load(f)

# Define the upload folder
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['image']
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Preprocess the image
        img = load_img(file_path, target_size=(150, 150))
        img_array = img_to_array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make predictions
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class = list(class_indices.keys())[predicted_class_index]

        return render_template('result.html', predicted_class=predicted_class, image_url=file_path)

# Route to handle pesticide recommendations
@app.route('/pesticide-recommendations', methods=['POST'])
def pesticide_recommendations():
    predicted_class = request.form.get('predicted_class')
    recommendations = get_pesticide_recommendations(predicted_class)

    return render_template('recommendations.html', predicted_class=predicted_class, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
