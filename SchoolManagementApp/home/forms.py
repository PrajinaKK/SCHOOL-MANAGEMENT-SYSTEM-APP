from django import forms
from django.core.validators import RegexValidator
from .models import Student
from accounts.models import School, Department,User

class StudentForm(forms.ModelForm):
    
    BLOODGROUP_CHOICES = (('A+','A+'),('B+','B+'))
    GENDER_CHOICES=(('F','Female'),('M','Male'))
    NATIONALITY_CHOICES=(('IN','INDIA'),('USA','AMERICA'))
    CATEGORY_CHOICES=(('SC/ST','SC/ST'),('OEC','OEC'),('OBC','OBC'))
    RELIGION_CHOICES=(('H','HINDU'),('C','CHRISTIAN'),('M','MUSLUM'))
    
    
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        widget=forms.Select(attrs={'class':'form-select','type' : ''}),
        # empty_label="Select a School",
        # label="School"
    )
    student_department=forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class':'form-select','type' : ''})
    )
    student_HOD = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=True),
        widget=forms.Select(attrs={'class':'form-select','type' : ''}),
       
    )
    student_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    student_dob=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'}))
    student_blood_group=forms.ChoiceField(choices=BLOODGROUP_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    nationality=forms.ChoiceField(choices=NATIONALITY_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    category=forms.ChoiceField(choices=CATEGORY_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    religion=forms.ChoiceField(choices=RELIGION_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    student_email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type' : 'email'}))
    student_phone_number=forms.IntegerField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (up to 10 digits)')],widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    student_photo=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    student_address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    student_paid_amount= forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    student_admission_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    student_joined_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'}))
    student_roll_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    student_parent_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    student_relation_with_parent=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    student_parent_occupation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    student_parent_email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type' : 'email'}))
    student_parent_phone_number=forms.IntegerField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (up to 10 digits)')],widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    student_parent_address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))

    class Meta:
        model = Student
        fields = [
            'school',
            'student_name',
            'student_dob',
            'student_blood_group',
            'gender',
            'nationality',
            'category',
            'religion',
            'student_email',
            'student_phone_number',
            'student_photo',
            'student_address',
            'student_paid_amount',
            'student_admission_number',
            'student_joined_date',
            'student_roll_number',
            'student_parent_name',
            'student_relation_with_parent',
            'student_parent_occupation',
            'student_parent_email',
            'student_parent_phone_number',
            'student_parent_address',
        ]