import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


class HealthPredictor:
    def __init__(self):
        self.model = None
        self.preprocessor = None
        self.features = [
            'Age', 'Gender', 'Height', 'Weight', 'BMI', 'Resting Heart Rate', 
            'Blood Pressure Systolic', 'Blood Pressure Diastolic', 'Respiratory Rate', 
            'Body Temperature', 'Blood Sugar Levels', 'Oxygen Saturation Levels', 
            'Medical Conditions', 'Medication Required'
        ]
        self.numerical_features = [
            'Age', 'Height', 'Weight', 'BMI', 'Resting Heart Rate', 
            'Blood Pressure Systolic', 'Blood Pressure Diastolic', 'Respiratory Rate', 
            'Body Temperature', 'Blood Sugar Levels', 'Oxygen Saturation Levels'
        ]
        self.categorical_features = ['Gender', 'Medical Conditions', 'Medication Required']
        self.new_data = None 
    
    def _build_preprocessor(self):
        """Builds a preprocessing pipeline for both numerical and categorical features."""
        numerical_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, self.numerical_features),
                ('cat', categorical_transformer, self.categorical_features)
            ]
        )
    
    def load_and_preprocess_data(self, file_path):
        data = pd.read_csv(file_path)
        X = data[self.features]
        y = data[['Blood Pressure Systolic', 'Blood Pressure Diastolic', 'Body Temperature', 'Blood Sugar Levels', 'Respiratory Rate']]
        self._build_preprocessor()
        X_processed = self.preprocessor.fit_transform(X)
        return train_test_split(X_processed, y, test_size=0.2, random_state=42)
    
    def build_model(self, input_shape):
        self.model = Sequential([
            Dense(128, activation='relu', input_shape=(input_shape,)),
            Dropout(0.2),
            Dense(64, activation='relu'),
            Dense(5, activation='linear')
        ])
        self.model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    def train_model(self, file_path):
        X_train, X_test, y_train, y_test = self.load_and_preprocess_data(file_path)
        self.build_model(X_train.shape[1])
        self.model.fit(X_train, y_train, epochs=50, validation_split=0.2, verbose=1)
        # print("Model training complete.")
    
    def predict(self, new_data):
        self.new_data = new_data
        new_data_processed = self.preprocessor.transform(new_data)
        # print("new data processed" )
        # print(new_data_processed)
        predictions = self.model.predict(new_data_processed)
        # print(predictions)
        return predictions


    def diagnose(self, predictions):
        # Extract predictions for each vital sign
        bp_systolic = self.new_data['Blood Pressure Systolic'].values[0] if 'Blood Pressure Systolic' in self.new_data.columns else predictions[0, 0]
        bp_diastolic = self.new_data['Blood Pressure Diastolic'].values[0] if 'Blood Pressure Diastolic' in self.new_data.columns else predictions[0, 1]
        temperature = self.new_data['Body Temperature'].values[0] if 'Body Temperature' in self.new_data.columns else predictions[0, 2]
        blood_sugar = self.new_data['Blood Sugar Levels'].values[0] if 'Blood Sugar Levels' in self.new_data.columns else predictions[0, 3]
        respiratory_rate = self.new_data['Respiratory Rate'].values[0] if 'Respiratory Rate' in self.new_data.columns else predictions[0, 4]

        # Define diagnosis categories based on thresholds
        diagnosis_categories = {
            'Blood Pressure': {
                'Low': (bp_systolic < 90) or (bp_diastolic < 60),
                'Normal': (90 <= bp_systolic <= 120) and (60 <= bp_diastolic <= 80),
                'High': (bp_systolic > 120) or (bp_diastolic > 80)
            },
            'Body Temperature': {
                'Low': temperature < 36.5,
                'Normal': 36.5 <= temperature <= 37.2,
                'High': temperature > 37.2
            },
            'Blood Sugar Levels': {
                'Low': blood_sugar < 70,
                'Normal': 70 <= blood_sugar <= 100,
                'High': blood_sugar > 100
            },
            'Respiratory Rate': {
                'Low': respiratory_rate < 12,
                'Normal': 12 <= respiratory_rate <= 20,
                'High': respiratory_rate > 20
            }
        }

        # Generate diagnosis messages for each vital sign
        diagnosis_messages = []
        for vital_sign, categories in diagnosis_categories.items():
            for category, condition in categories.items():
                if condition:
                    diagnosis_messages.append(f"{vital_sign} is {category}")

        # Combine diagnosis messages
        diagnosis = ', '.join(diagnosis_messages)

        return diagnosis
    
