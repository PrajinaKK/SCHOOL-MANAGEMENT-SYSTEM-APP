from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User, School,Position,Department

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    
    list_display = ['username','email','first_name']

admin.site.register(User,UsersAdmin)
admin.site.register(School)

admin.site.register(Position)
admin.site.register(Department)

