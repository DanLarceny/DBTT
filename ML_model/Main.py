from Model import HealthPredictor
import pandas as pd 


# Instantiate the HealthPredictor
predictor = HealthPredictor()

# Train the model with a CSV file containing training data
predictor.train_model('first_5000_rows_healthcare_data.csv')

# Example new patient data (adjust the fields as necessary)
new_patient_data = pd.DataFrame({
    'Age': [50],
    'Gender': ['Male'],  # This will be encoded automatically
    'Height': [170],
    'Weight': [70],
    'BMI': [24.2],
    'Resting Heart Rate': [75],
    'Blood Pressure Systolic': [120],
    'Blood Pressure Diastolic': [80],
    'Respiratory Rate': [18],
    'Body Temperature': [39],
    'Blood Sugar Levels': [110],
    'Oxygen Saturation Levels': [98],
    'Medical Conditions': ['None'],
    'Medication Required': ['No']
})

# Make a prediction
predictions = predictor.predict(new_patient_data)

# Generate a diagnosis
diagnosis = predictor.diagnose(predictions)
print("this is diagnosis")
print(diagnosis)
