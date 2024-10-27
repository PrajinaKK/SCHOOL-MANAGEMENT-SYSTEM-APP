from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name="staff"
urlpatterns = [
   path("staffs/",StaffListView.as_view(),name="staff-list"),
   path('update/<slug:slug>',StaffUpdateView.as_view(),name="update-staff"),
   path('delete/<slug:slug>/', DeleteStaffView.as_view(), name="delete-staff")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)