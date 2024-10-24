from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,FormView
from django.contrib.auth import authenticate,login,logout
from . forms import SignUpForm,SchoolDetailsForm,LoginForm
from django.urls import reverse_lazy,reverse
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.
class LoginView(FormView):
    template_name = "login/login.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home:dashboard") 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = SignUpForm()
        context['login_form'] = LoginForm()
        return context
    
    
    def form_valid(self, form):
        print(self.request.POST)
        password = form.cleaned_data.get('password')
        username=form.cleaned_data.get('first_name')
        confirm_password = form.cleaned_data.get('confirm_password')
        if 'login' in self.request.POST:
            user = form.get_user()
            # email = self.request.POST["email"]
            # username=User.objects.get(email=email).username
            # user=authenticate(username=username,password=password)
            if user:
                print('user',user)
                login(self.request, user)
                print("user success logined")
            else:
                return reverse_lazy("accounts:login")   
       

        if password and confirm_password and password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match.")
            return self.form_invalid(form)
       
        user = form.save(commit=False)
        user.set_password(password)
        user.username = username
        if self.request.POST['roles'] == "A":
            user.is_superuser = True
        user.save()
           
        login(self.request, user)

        if user.is_superuser:
            return HttpResponseRedirect(reverse("accounts:schooldetails"))
        
        return redirect(self.success_url)
        
        


class SchoolDetailsView(FormView):
    template_name = "login/schooldetails.html"
    form_class=SchoolDetailsForm





# <QueryDict: {'csrfmiddlewaretoken': ['hh3Qh7lfxcUu8kwPBbHrRXy3mGCTQ6Vw75X0jkfNpUqmkF8Y7SvQq6hmZMRjXzix'], 
#              'roles': ['A'], 
#              'first_name': ['Malu'], 
#              'age': ['24'], 
#              'email': ['malu@gmail.com'],
#                'DOB': ['1997-06-19'], 
#                'Address': ['Miracle,Thillenkery,Kannur,Kannur,Kerala'],
#               'last_name': ['M'], 
#               'phone_number': ['09087654322'], 
#               'gender': ['F'], 
#               'password': ['zxcvbnm'],
#                 'confirm_password': ['zxcvbnm'], 
#                 'sign-up': ['']}>
    