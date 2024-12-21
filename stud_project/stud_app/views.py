from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from django.views import View
from .models import *
from django.contrib.auth import authenticate

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print("Received username:", username)
        print("Received password:", password)

       
        user = authenticate(username=username, password=password)
        print("Authenticated user:", user)

        if user:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)





class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

from django.http import JsonResponse

def test_view(request):
    print("error")
    return JsonResponse({"message": "Hello, world!"})


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Attendance
from django.contrib.auth.models import User

@api_view(['POST'])
def mark_attendance(request):
    student_id = request.data.get('student_id')
    date = request.data.get('date')
    attendance_status = request.data.get('status') 

    if not student_id or not date or attendance_status is None:
        return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        student = StudUser.objects.get(id=student_id)
    except StudUser.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

   
    attendance, created = Attendance.objects.update_or_create(
        student=student,
        date=date,
        defaults={'status': attendance_status}
    )

    if created:
        return Response({"message": "Attendance marked successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Attendance updated successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def attendance_percentage(request, student_id):
    try:
        student = StudUser.objects.get(id=student_id) 
    except StudUser.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    total_days = Attendance.objects.filter(student=student).count()
    present_days = Attendance.objects.filter(student=student, status=True).count()

    if total_days == 0:
        return Response({"message": "No attendance records found for this student."}, status=status.HTTP_404_NOT_FOUND)

    percentage = (present_days / total_days) * 100
    return Response({"student": student.username, "attendance_percentage": percentage}, status=status.HTTP_200_OK)



    
def mark_attendance_page(request):
    return render(request, 'mark_attendance.html')

def attendance_report_page(request):
    return render(request, 'attendance_report.html')