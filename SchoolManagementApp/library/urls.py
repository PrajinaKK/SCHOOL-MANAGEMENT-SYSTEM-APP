from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name="library"
urlpatterns = [
   path("add/books/",BookFormView.as_view(),name="add-book"),
   path("update/books/<slug:slug>",BookUpdateView.as_view(),name="update-book"),
   path('book-list/', BookListView.as_view(),name="book-list"),
   path('delete/<slug:slug>/',BookDeleteView.as_view(), name="delete-book")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)