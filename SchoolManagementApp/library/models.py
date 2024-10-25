from django.db import models
from home.models import Student
from accounts.models import User,School
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class BookGenre(models.Model):
    genre=models.CharField(max_length=100)
    def __str__(self):
        return self.genre

class Books(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    librarian=models.ForeignKey(User,on_delete=models.CASCADE,related_name="library")
    school = models.OneToOneField(School,on_delete=models.CASCADE,related_name="books")
    book_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, null=True)
    book_author=models.CharField(max_length=100)
    total_books=models.IntegerField()
    book_genre = models.OneToOneField(BookGenre,on_delete=models.CASCADE,related_name="book")
    book_price=models.IntegerField()
    book_image=models.ImageField(upload_to="image_of_book/")
    book_number=models.IntegerField()
    number_of_copies=models.IntegerField()
    borrowed_by=models.ManyToManyField(Student,related_name="borrowed_book")
    borrowed_date=models.DateField()
    number_of_copies_available=models.IntegerField()
    total_books=models.IntegerField()

    created_at=models.DateTimeField(null=True, auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    def __str__(self):
        return self.book_name
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)
        super().save(*args, *kwargs)    