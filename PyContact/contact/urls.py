from django.urls import path, include
from .views import index, ContactView
from .models import Contact

urlpatterns = [
    path('', index),
    path('contact', ContactView.as_view(model=Contact))
]