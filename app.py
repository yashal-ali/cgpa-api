from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

# Load the model
model = pickle.load(open('first_gpa.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Grade mapping
grade_map = {'A+':4.0, 'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7,
             'C+':2.3, 'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0.0, 'WU':0.0, 'W':0.0}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # Convert grades to numerical values
        grades = [grade_map.get(data.get(f'c{i+1}'), 0.0) for i in range(11)]
        prediction = model.predict(np.array(grades).reshape(1, -1))
        result = round(float(prediction[0][0]), 2)
        return jsonify({'cgpa': result})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()

