from django import forms
from accounts.models import User,School
from home.models import Student
from . models import BookGenre,Books

class BookForm(forms.ModelForm):
    
    librarian = forms.ModelChoiceField(queryset=User.objects.filter(is_librarian=True),widget=forms.Select(attrs={'class':'form-select'}))
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        widget=forms.Select(attrs={'class':'form-select','type' : ''}),
        
    )
    book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    book_author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'text'}))
    book_genre=forms.ModelChoiceField(
        queryset=BookGenre.objects.all(),
        widget=forms.Select(attrs={'class':'form-select','type' : ''}),
        
    )
    book_price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    book_image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    book_number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    number_of_copies=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    number_of_copies_available=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','type' : ''}))
    borrowed_by=forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.SelectMultiple(attrs={'class':'form-select','type' : ''}),
        
    )
    borrowed_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type' : 'date'}))

    class Meta:
        model = Books
    
        fields=['librarian','school','book_name','book_author','book_genre','book_price','book_image','book_number','number_of_copies','number_of_copies_available','borrowed_by','borrowed_date']