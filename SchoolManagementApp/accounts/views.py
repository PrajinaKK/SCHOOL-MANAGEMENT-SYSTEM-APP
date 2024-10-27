from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,FormView
from django.contrib.auth import authenticate,login,logout
from . forms import SignUpForm,SchoolDetailsForm,LoginForm,MoreAboutForm
from django.urls import reverse_lazy,reverse
from .models import User,School
from django.http import HttpResponseRedirect

# Create your views here.
class LoginView(FormView):
    template_name = "login/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("accounts:moreaboutuser") 
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = SignUpForm()
        context['login_form'] = LoginForm()
        return context
    
    
    def form_valid(self, form):
        print(self.request.POST)
        password = form.cleaned_data.get('password')
        username=form.cleaned_data.get('first_name')
        print(username)
        confirm_password = form.cleaned_data.get('confirm_password')
        if 'login' in self.request.POST:
            # user = form.get_user()
            email = self.request.POST["email"]
            username=User.objects.get(email=email).username
            user=authenticate(username=username,password=password)
            if user:
                print('user',user)
                login(self.request, user)
                print("user success logined")
                return HttpResponseRedirect(reverse("home:dashboard"))
            else:
                return reverse_lazy("accounts:login")   
       

        if password and confirm_password and password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match.")
            return self.form_invalid(form)
       
        user = form.save(commit=False)
        user.set_password(password)
        print(user.set_password(password))
        user.username = username
        print(user)
        print(user.username)
        if self.request.POST['roles'] == "A":
            user.is_superuser = True
        if self.request.POST['roles'] == "S":
            user.is_staff = True 
        if self.request.POST['roles'] == "L":
            user.is_librarian = True    
        user.save()
           
        login(self.request, user)

        

        if user.is_superuser:
            return HttpResponseRedirect(reverse("accounts:schooldetails"))
        
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form)
    
        
        


class SchoolDetailsView(FormView):
    template_name = "login/schooldetails.html"
    form_class=SchoolDetailsForm
    success_url = reverse_lazy("home:dashboard")
    def form_valid(self, form):

        school_name = form.cleaned_data.get('school_name')
        print(school_name)
        user=self.request.user
        print(user)
        print(user.school)
        
        print(self.request.POST)
        if self.request.user.is_authenticated:
            form.save()
    
        school = School.objects.get(school_name=school_name)
        user.school = school    
        user.save()

        return redirect(self.success_url)
    
    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form)     
            
class MoreAboutUser(FormView):
    template_name="login/moreabout.html"
    form_class=MoreAboutForm
    success_url = reverse_lazy("home:dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs.update({
                'instance': self.request.user,
                'data': self.request.POST or None,
            })
        else:
            kwargs.update({
                'data': self.request.POST or None,
            })
        return kwargs
    def form_valid(self, form):
        print(self.request.POST)
        if self.request.user.is_authenticated:
            form.save()
        return redirect(self.success_url)




