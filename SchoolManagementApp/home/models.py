from django.db import models
from accounts.models import User,School
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
# from library.models import Books
# Create your models here.

class Student(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    FEESTATUS_CHOICES=(('P','Paid'),('U','Unpaid'))
    BLOODGROUP_CHOICES = (('A+','A+'),('B+','B+'))
    GENDER_CHOICES=(('F','Female'),('M','Male'))
    NATIONALITY_CHOICES=(('IN','INDIA'),('USA','AMERICA'))
    CATEGORY_CHOICES=(('SC/ST','SC/ST'),('OEC','OEC'),('OBC','OBC'))
    RELIGION_CHOICES=(('H','HINDU'),('C','CHRISTIAN'),('M','MUSLUM'))
    school=models.OneToOneField(School,on_delete=models.CASCADE,related_name="student")
    student_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True)
    student_dob=models.DateField()
    student_blood_group=models.CharField(max_length=2,choices=BLOODGROUP_CHOICES)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)	
    nationality=models.CharField(max_length=3,choices=NATIONALITY_CHOICES)
    category=models.CharField(max_length=10,choices=CATEGORY_CHOICES)
    religion=models.CharField(max_length=1,choices=RELIGION_CHOICES)
    student_email=models.EmailField()
    student_phone_number=models.CharField(max_length=10)
    student_photo=models.ImageField(upload_to="student_photo/")
    student_address=models.CharField(max_length=255)
    student_paid_amount = models.IntegerField()
    student_admission_number=models.IntegerField()
    student_joined_date=models.DateField()
    student_roll_number=models.IntegerField()
    student_parent_name=models.CharField(max_length=50)
    student_relation_with_parent=models.CharField(max_length=50)
    student_parent_occupation=models.CharField(max_length=50)
    student_parent_email=models.EmailField(null=True)
    student_parent_phone_number=models.CharField(max_length=10)
    student_parent_address=models.CharField(max_length=255)

    
    fee_paid_date=models.DateTimeField(auto_now=True)
    fee_status=models.CharField(choices=FEESTATUS_CHOICES,max_length=1,null=True)
    
    created_at=models.DateTimeField(null=True, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.student_name)
        super().save(*args,**kwargs) 


    def __str__(self):
        return self.student_name
    
    def get_url(self):
        return reverse('home:update_student',args=[self.slug])
    def get_url_of_student(self):
        return reverse('home:delete_student',args=[self.slug])