from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User

class StudUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username



class Attendance(models.Model):
    student = models.ForeignKey(StudUser, on_delete=models.CASCADE)  # Assuming you're using User for students
    date = models.DateField()
    status = models.BooleanField(default=False)  # True = Present, False = Absent

    def __str__(self):
        return f"{self.student.username} - {self.date} - {'Present' if self.status else 'Absent'}"
