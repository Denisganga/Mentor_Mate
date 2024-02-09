from django.urls import path
from .views import Register

urlpatterns = [
    path('register/', Register, name='register'),
]