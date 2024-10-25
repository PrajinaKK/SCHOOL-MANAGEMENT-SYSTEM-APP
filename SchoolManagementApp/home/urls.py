from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name="home"
urlpatterns = [
    path('dashboard/',DashboardView.as_view(),name="dashboard"),
    path('add_student/',AddStudentView.as_view(),name="add_student"),
    path('newStaff/',NewStaffAddView.as_view(), name="newstaff"),
    path('newLibrarian/',NewLibrarianAddView.as_view(), name="newlibrarian"),
    path("update/student/<slug:slug>", UpdateStudentView.as_view(),name="update_student"),
    path('delete/<slug:slug>', DeleteStudentView.as_view(),name="delete_student")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)