import requests

# The URL for the predict endpoint
url = "http://127.0.0.1:5000/predict"

# The data to send with the request
data = {
    "Age": [50],
    "Gender": ["Male"],
    "Height": [170],
    "Weight": [70],
    "BMI": [24.2],
    "Resting Heart Rate": [75],
    "Blood Pressure Systolic": [120],
    "Blood Pressure Diastolic": [80],
    "Respiratory Rate": [18],
    "Body Temperature": [39],
    "Blood Sugar Levels": [110],
    "Oxygen Saturation Levels": [98],
    "Medical Conditions": ["None"],
    "Medication Required": ["No"]
}

# Make the POST request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print("Response Body:")
print(response.json())