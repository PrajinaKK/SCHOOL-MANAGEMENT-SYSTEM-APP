from django.shortcuts import render,redirect
from . forms import StudentForm
from accounts.forms import SignUpForm,MoreAboutForm
from .models import Student,School
from accounts.models import User
from library.models import Books
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView,ListView


# Create your views here.
class DeleteStudentView(LoginRequiredMixin,DeleteView):
    model = Student
    
    success_url = reverse_lazy('home:dashboard')
    slug_field = 'slug'  # Tell Django to look for the slug field in the model
    slug_url_kwarg = 'slug'  # The URL parameter to capture the slug

    def post(self, request, *args, **kwargs):

        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this school.")
        
        self.object = self.get_object()
        
        
        self.object.delete()
        
        return redirect(self.success_url)

class UpdateStudentView(LoginRequiredMixin, UpdateView):
    template_name = "forms/updateStudent.html"
    form_class=StudentForm
    # context_object_name="form"
    model= Student
    slug_field = 'slug'
    slug_url_kwarg= 'slug'
    success_url = reverse_lazy("home:dashboard")

class StudentListView(LoginRequiredMixin, ListView):
   
    template_name = "dashboard/student-list.html"
    queryset=Student.objects.all()
    context_object_name = "students"

class DashboardView(LoginRequiredMixin, ListView):
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
        if user.is_superuser:
            context["is_superuser"] = True

        return context
    

class AddStudentView(LoginRequiredMixin, FormView):
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

class NewStaffAddView(LoginRequiredMixin, FormView):
    template_name = "forms/newstaff.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = context.get("form",SignUpForm)
        context["form_two"] = context.get("form_two",MoreAboutForm)
        return context
    def post(self, request, *args, **kwargs):
         
        
        form_one = SignUpForm(request.POST,instance=request.user)
        form_two = MoreAboutForm(request.POST,request.FILES,instance=request.user)
        print(self.request.POST)
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        

        if password and confirm_password and password != confirm_password:
            form_one.add_error('confirm_password', "Passwords do not match.")
            return self.form_invalid(form_one)

        if form_one.is_valid() and form_two.is_valid():
            
            return self.forms_valid(form_one,form_two)
        else:
            return self.forms_invalid(form_one, form_two)

    def forms_valid(self, form_one,form_two):
        password = form_one.cleaned_data.get('password')
        username=form_one.cleaned_data.get('first_name')
        user = form_one.save(commit=False)
        user.username = username
        user.set_password(password)
        

        print(user)
        print(user.username)
        if self.request.POST['roles'] == "A":
            user.roles = "A"
            user.is_superuser = True
        if self.request.POST['roles'] == "S":
            user.roles = "S"
            user.is_staff = True 
        if self.request.POST['roles'] == "L":
            user.roles = "L"
            user.is_librarian = True    
        user.save()
        
        form_two.save()
       
        print("both form success fully saved")

        return redirect(self.success_url)
    
    def form_invalid(self, form_one, form_two):
        print("Form 2 is invalid:  ", form_two.errors)
        print("form one error:  ", form_one.errors)
        return super().form_invalid(form_one)
    
  

   
        

  
class NewLibrarianAddView(LoginRequiredMixin ,FormView):
    template_name = "forms/newlibrarian.html"
    form_class = SignUpForm


