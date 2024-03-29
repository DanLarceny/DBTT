document.getElementById("healthForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Collect form data
    var formData = {
        "Age": [parseFloat(document.getElementById("age").value)],
        "Gender": [document.getElementById("gender").value],
        "Height": [parseFloat(document.getElementById("height").value)],
        "Weight": [parseFloat(document.getElementById("weight").value)],
        "BMI": [parseFloat(document.getElementById("bmi").value)],
        "Resting Heart Rate": [parseFloat(document.getElementById("resting_hr").value)],
        "Blood Pressure Systolic": [parseFloat(document.getElementById("blood_pressure_systolic").value)],
        "Blood Pressure Diastolic": [parseFloat(document.getElementById("blood_pressure_diastolic").value)],
        "Respiratory Rate": [parseFloat(document.getElementById("respiratory_rate").value)],
        "Body Temperature": [parseFloat(document.getElementById("body_temperature").value)],
        "Blood Sugar Levels": [parseFloat(document.getElementById("blood_sugar_levels").value)],
        "Oxygen Saturation Levels": [parseFloat(document.getElementById("oxygen_saturation_levels").value)],
        "Medical Conditions": [document.getElementById("medical_conditions").value],
        "Medication Required": [document.getElementById("medication_required").value]
        // Add more fields as needed
    };

    // Log the form data to the console
    console.log(formData);

    // Make POST request to Flask backend
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
.then(response => response.json())
.then(data => {
    console.log(data)
    // Display prediction result
    document.getElementById("result").innerText = "Diagnosis: " + data;
})
.catch((error) => {
    console.error('Error:', error);
});
});
