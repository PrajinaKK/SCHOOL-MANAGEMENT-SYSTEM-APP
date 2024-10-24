from django import forms
from django.core.validators import RegexValidator
from .models import User,School

class LoginForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type' : 'email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type' : 'password'}))
    
    class Meta:
        model = User
        fields = ['email','password']

        def clean(self):
            fields = self.cleaned_data  

class SignUpForm(forms.ModelForm):
    ROLES_CHOICES = (('A','Admin'),('S','Staff'),('L','Librarian'))
    GENDER_CHOICES=(('F','Female'),('M','Male'))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type':'number'}))
    phone_number=forms.IntegerField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (up to 10 digits)')],widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type' : 'email'}))
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    DOB=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'}))
    Address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    roles=forms.ChoiceField(choices=ROLES_CHOICES,widget=forms.RadioSelect(attrs={'class':'form-check-input radio','type' : 'radio'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type' : 'password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type' : 'password'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','age','phone_number','email','gender','DOB','Address','password','confirm_password']

        def clean(self):
            fields = self.cleaned_data     

class SchoolDetailsForm(forms.ModelForm):
    SCHOOLTYPE_CHOICES= (('A','Aided'),('U','UnAided'),('G','Government'))
    school_code = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    school_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    school_principal = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    tel=forms.IntegerField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (up to 10 digits)')],widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','type' : 'email'}))
    school_logo=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    school_image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    total_Staff = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    total_students=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    total_fee=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    class Meta:
        model = School
   
        fields = ['school_code','school_principal','tel','school_logo','email','school_image','total_Staff','total_students','address','total_fee']

        def clean(self):
            fields = self.cleaned_data                 