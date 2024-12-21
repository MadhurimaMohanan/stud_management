document.getElementById('attendanceReportForm').addEventListener('submit', function(event) {
    event.preventDefault();  

    const studentId = document.getElementById('studentId').value;
    const attendanceResult = document.getElementById('attendanceResult');

    
    attendanceResult.textContent = '';

   
    if (!studentId) {
        attendanceResult.textContent = 'Please enter a valid Student ID.';
        return;
    }

    
    fetch(`http://127.0.0.1:8000/api/stud_app/attendance-percentage/${studentId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')  // CSRF token for security
        },
        credentials: 'include'  
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            attendanceResult.textContent = `Error: ${data.error}`;
        } else {
            
            attendanceResult.innerHTML = `
                <p><strong>Student:</strong> ${data.student}</p>
                <p><strong>Attendance Percentage:</strong> ${data.attendance_percentage.toFixed(2)}%</p>
            `;
        }
    })
    .catch(error => {
        console.error('Error fetching attendance report:', error);
        attendanceResult.textContent = 'An error occurred. Please try again.';
    });
});
