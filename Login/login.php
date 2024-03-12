<?php
// Simulating user data (replace this with your actual user data or database connection)
$users = array(
    array('id' => 1, 'username' => 'patient1', 'password' => 'password1', 'userType' => 'patient'),
    array('id' => 2, 'username' => 'doctor1', 'password' => 'password2', 'userType' => 'doctor'),
);

// Function to validate user credentials
function validateUser($username, $password, $userType) {
    global $users;
    foreach ($users as $user) {
        if ($user['username'] === $username && $user['password'] === $password && $user['userType'] === $userType) {
            return $user;
        }
    }
    return null;
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check which form was submitted (login or signup)
    $formType = isset($_POST['formType']) ? $_POST['formType'] : '';

    // Handle login form
    if ($formType === 'login') {
        $username = isset($_POST['username']) ? $_POST['username'] : '';
        $password = isset($_POST['password']) ? $_POST['password'] : '';
        $userType = isset($_POST['userType']) ? $_POST['userType'] : 'patient'; // Set default to 'patient'

        // Validate user credentials
        $user = validateUser($username, $password, $userType);

        if ($user !== null) {
            // Login successful
            echo json_encode(array('success' => true, 'message' => 'Login successful', 'userType' => $user['userType']));
        } else {
            // Login failed
            echo json_encode(array('success' => false, 'message' => 'Invalid username, password, or user type'));
        }
    }
    // Handle signup form (you can implement this if needed)
    else if ($formType === 'signup') {
        // Handle signup logic here
        echo json_encode(array('success' => false, 'message' => 'Signup functionality not implemented'));
    } else {
        // Invalid form type
        echo json_encode(array('success' => false, 'message' => 'Invalid form type'));
    }
} else {
    // If the request is not a POST request
    echo json_encode(array('success' => false, 'message' => 'Invalid request method'));
}
?>
