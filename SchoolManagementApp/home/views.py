from django.shortcuts import render
from . forms import StudentForm
from accounts.forms import SignUpForm

# Create your views here.

from django.views.generic import TemplateView,FormView


# Create your views here.
class DashboardView(TemplateView):
    template_name = "dashboard/home.html"
   
   

class AddStudentView(FormView):
    template_name = "forms/forms.html"
    form_class = StudentForm

class NewStaffAddView(FormView):
    template_name = "forms/newstaff.html"
    form_class = SignUpForm

  
class NewLibrarianAddView(FormView):
    template_name = "forms/newlibrarian.html"
    form_class = SignUpForm
