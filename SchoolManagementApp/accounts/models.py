from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class School(models.Model):
    SCHOOLTYPE_CHOICES= (('A','Aided'),('U','UnAided'),('G','Government'))
    school_code = models.IntegerField()
    school_name= models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    school_principal=models.CharField(max_length=100)
    tel=models.CharField(max_length=10)
    email=models.EmailField()
    school_logo = models.ImageField(upload_to="logo/")
    school_image = models.ImageField(upload_to="schoolimage/")
    total_Staff = models.IntegerField()
    total_students = models.IntegerField()
    total_fee = models.IntegerField()

    def __str__(self):
        return self.school_name
    
class User(AbstractUser):
    ROLES_CHOICES = (('A','Admin'),('S','Staff'),('L','Librarian'))
    GENDER_CHOICES=(('F','Female'),('M','Male'))
    POSITION_CHOICES=(('F','Faculty'),('C','CLERK'))
    age=models.SmallIntegerField(null=True)
    dob=models.DateField(null=True)
    phone_number=models.CharField(max_length=10,blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)	
    address=models.CharField(max_length=255,blank=True)
    is_librarian = models.BooleanField(default=False)
    roles=models.CharField(max_length=1,choices=ROLES_CHOICES,blank=True)	
    school = models.OneToOneField(School,on_delete=models.CASCADE,null=True,related_name="school")


