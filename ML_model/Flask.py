from flask import Flask, request, jsonify
from Model import HealthPredictor  # Assuming this is your custom model class
import pandas as pd

app = Flask(__name__)

# Instantiate the HealthPredictor
predictor = HealthPredictor()

# Assuming the model needs to be trained only once and used for prediction multiple times
# If the training data is not too large, it might be okay to load it at the start.
# Otherwise, consider training the model outside the app and loading the trained model instead.
predictor.train_model('ML_model/first_5000_rows_healthcare_data.csv')


@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the POST request
    data = request.get_json(force=True)
    
    # Convert data to DataFrame
    new_patient_data = pd.DataFrame(data)
    
    # Make a prediction
    predictions = predictor.predict(new_patient_data)
    
    # Generate a diagnosis
    diagnosis = predictor.diagnose(predictions)
    
    return jsonify(diagnosis)


if __name__ == '__main__':
    # Define the host and port explicitly
    host = '127.0.0.1'
    port = 5000

    # Print the URL and port information before running the app
    print(f"Running Flask app on http://{host}:{port}")
    
    app.run(host=host, port=port, debug=False)
