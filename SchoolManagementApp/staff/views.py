from django.shortcuts import render,redirect
from django.views.generic import ListView,UpdateView,DeleteView
from accounts.models import User
from accounts.forms import UserForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
# Create your views here.

class StaffListView(ListView):
    template_name = "staff/staff-list.html"
    queryset=User.objects.all()
    context_object_name = "staffs"

class StaffUpdateView(UpdateView):
    template_name = "staff/updateStaff.html"
    form_class=UserForm
    # context_object_name="form"
    model= User
    slug_field = 'slug'
    slug_url_kwarg= 'slug'
    success_url = reverse_lazy("home:dashboard")    

class DeleteStaffView(DeleteView):
    model = User
    
    success_url = reverse_lazy('home:dashboard')
    slug_field = 'slug'  # Tell Django to look for the slug field in the model
    slug_url_kwarg = 'slug'  # The URL parameter to capture the slug

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("ysed posted")

        if not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this school.")
        
        self.object = self.get_object()
        print("this is the data to be deleted: ",self.object)
        
        
        self.object.delete()
        
        return redirect(self.success_url)
