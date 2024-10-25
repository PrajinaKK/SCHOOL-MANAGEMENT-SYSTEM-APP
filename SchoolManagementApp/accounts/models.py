from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class School(models.Model):

    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    SCHOOLTYPE_CHOICES= (('A','Aided'),('U','UnAided'),('G','Government'))
    school_code = models.IntegerField()
    school_type=models.CharField(choices=SCHOOLTYPE_CHOICES,max_length=1,blank=True)
    
    school_name= models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,null=True)

    address=models.CharField(max_length=255)
    school_principal=models.CharField(max_length=100)
    tel=models.CharField(max_length=10)
    email=models.EmailField()
    school_logo = models.ImageField(upload_to="logo/")
    school_image = models.ImageField(upload_to="schoolimage/")
    total_Staff = models.IntegerField()
    total_students = models.IntegerField()
    total_fee = models.IntegerField()

    created_at=models.DateTimeField(null=True, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self):
        return self.school_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.school_name)
        super().save(*args, **kwargs)       
    
class Position(models.Model):
    position=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.position
    
class Department(models.Model):
    department=models.CharField(max_length=20,unique=True)   
    def __str__(self):
        return self.department 

 
    
class User(AbstractUser):
    ROLES_CHOICES = (('A','Admin'),('S','Staff'),('L','Librarian'))
    GENDER_CHOICES=(('F','Female'),('M','Male'))

    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    slug=models.SlugField(max_length=150,null=True)
    age=models.SmallIntegerField(null=True)
    dob=models.DateField(null=True)
    phone_number=models.CharField(max_length=10,blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)	
    address=models.CharField(max_length=255,blank=True)
    is_librarian = models.BooleanField(default=False)
    roles=models.CharField(max_length=1,choices=ROLES_CHOICES,blank=True)	
    school = models.OneToOneField(School,on_delete=models.CASCADE,null=True,related_name="users")
    position=models.OneToOneField(Position,on_delete=models.CASCADE,null=True,related_name="staffs")
    department=models.OneToOneField(Department,on_delete=models.CASCADE,null=True,related_name="faculty_members")
    joined_date=models.DateField(null=True)
    user_photo=models.ImageField(upload_to="user_photo/",null=True)

    created_at=models.DateTimeField(null=True, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)    
    




