document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

   
    const csrfToken = document.querySelector('meta[name="csrf-token"]');

    if (!csrfToken || !csrfToken.getAttribute('content')) {
        console.error('CSRF token is missing!');
        return;
    }

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

   
    errorMessage.textContent = '';

    if (!username || !password) {
        errorMessage.textContent = 'Please fill in both fields.';
        return;
    }

   
    fetch('http://127.0.0.1:8000/api/stud_app/login-api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken.getAttribute('content')  
        },
        body: JSON.stringify({
            username: username,
            password: password
        }),
        credentials: 'include'  
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Invalid credentials or server error');
        }
        return response.json();
    })
    .then(data => {
        if (data.message === "Login successful") {
            window.location.href = '/mark-attendance-page/';  
        } else {
            errorMessage.textContent = 'Invalid credentials. Please try again.';
        }
    })
    .catch(error => {
        console.error('Error during login:', error);  
        errorMessage.textContent = 'An error occurred. Please try again.';
    });
});
