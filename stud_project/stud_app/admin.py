from django.contrib import admin

# Register your models here.

from .models import StudUser,Attendance

@admin.register(StudUser)
class StudUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

from .models import Attendance
admin.site.register(Attendance)
