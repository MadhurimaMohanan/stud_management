document.getElementById('attendanceForm').addEventListener('submit', function(event) {
    event.preventDefault();  

   
    const studentId = document.getElementById('studentId').value;
    const date = document.getElementById('date').value;
    const status = document.getElementById('status').value;

    const errorMessage = document.getElementById('errorMessage');
    const successMessage = document.getElementById('successMessage');

   
    errorMessage.textContent = '';
    successMessage.textContent = '';

   
    if (!studentId || !date || !status) {
        errorMessage.textContent = 'Please fill in all fields.';
        return;
    }

  
    fetch('http://127.0.0.1:8000/api/stud_app/mark-attendance/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')  // Add CSRF token here
        },
        body: JSON.stringify({
            student_id: studentId,
            date: date,
            status: status === 'true' 
        }),
        credentials: 'include' 
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            successMessage.textContent = data.message;
        } else if (data.error) {
            errorMessage.textContent = data.error;
        }
    })
    .catch(error => {
        console.error('Error during attendance marking:', error);
        errorMessage.textContent = 'An error occurred. Please try again.';
    });
});
