# stud_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('login-api/', LoginAPIView.as_view(), name='login-api'),
    path('test/', test_view),  # Test URL to check if routes are working
    path('mark-attendance/', mark_attendance),
    path('attendance-percentage/<int:student_id>/',attendance_percentage),
    
]
