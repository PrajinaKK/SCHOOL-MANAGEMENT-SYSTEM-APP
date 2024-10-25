from django.shortcuts import render,redirect
from . forms import StudentForm
from accounts.forms import SignUpForm
from .models import Student,School
from accounts.models import User
from library.models import Books
from django.db.models import Q
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView,ListView


# Create your views here.
class DeleteStudentView(DeleteView):
    model = Student
    
    success_url = reverse_lazy('home:dashboard')
    slug_field = 'slug'  # Tell Django to look for the slug field in the model
    slug_url_kwarg = 'slug'  # The URL parameter to capture the slug

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        self.object.delete()
        
        return redirect(self.success_url)

class UpdateStudentView(UpdateView):
    template_name = "forms/updateStudent.html"
    form_class=StudentForm
    # context_object_name="form"
    model= Student
    slug_field = 'slug'
    slug_url_kwarg= 'slug'
    success_url = reverse_lazy("home:dashboard")


class DashboardView(ListView):
    template_name = "dashboard/home.html"
    queryset=Student.objects.all()
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['total_students'] = Student.objects.count()
        context['total_staff'] = User.objects.count()
        context['total_books'] = Books.objects.count()
        context['staffs'] = User.objects.filter(~Q(is_superuser=True)).order_by('-created_at')

        return context
    

class AddStudentView(FormView):
    template_name = "forms/forms.html"
    form_class = StudentForm
    success_url = reverse_lazy("home:add_student")

    def form_valid(self, form):
        student_form= StudentForm()
       
        if self.request.user.is_authenticated:
            form.save()
          
        return redirect(self.success_url) 
        
    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form)     

class NewStaffAddView(FormView):
    template_name = "forms/newstaff.html"
    form_class = SignUpForm

  
class NewLibrarianAddView(FormView):
    template_name = "forms/newlibrarian.html"
    form_class = SignUpForm


