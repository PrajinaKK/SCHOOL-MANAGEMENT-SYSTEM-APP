from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name="accounts"
urlpatterns = [
    path('',LoginView.as_view(), name="login"),
    path('schooldetails/',SchoolDetailsView.as_view(), name="schooldetails")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
