from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    
    list_display = ['school','student_name','student_email']


admin.site.register(Student,StudentAdmin)
