from django.urls import path
from .views import Register

app_name='authentication'

urlpatterns = [
    path('register/', Register, name='register'),
]