from django.shortcuts import render,redirect
from django.views.generic import FormView,UpdateView,ListView,DeleteView

from . forms import BookForm
from django.urls import reverse_lazy
from .models import Books
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BookFormView(LoginRequiredMixin, FormView):
    template_name="addBooks.html"
    form_class = BookForm
    success_url = reverse_lazy("home:dashboard")# change it to book list later

    def form_valid(self, form):
        book_form= BookForm()
       
        if self.request.user.is_authenticated:
            user = form.save(commit=False)
            user.total_books = Books.objects.count()+1
            user.save()
          
        return redirect(self.success_url) 
        
    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form)       

class BookListView(LoginRequiredMixin,ListView):
    template_name= "book-list.html"    
    queryset = Books.objects.all()
    context_object_name = "books"
    

class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "updateBooks.html"
    form_class=BookForm
    # context_object_name="form"
    model= Books
    slug_field = 'slug'
    slug_url_kwarg= 'slug'
    success_url = reverse_lazy("home:dashboard")

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    
    success_url = reverse_lazy('library:book-list')
    slug_field = 'slug'  # Tell Django to look for the slug field in the model
    slug_url_kwarg = 'slug'  # The URL parameter to capture the slug

    def post(self, request, *args, **kwargs):
        print("yes posted")

        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this school.")
        
        self.object = self.get_object()
        print("object to be deleted: ",self.object)
        
        
        self.object.delete()
        
        return redirect(self.success_url)
