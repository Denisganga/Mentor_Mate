from django.urls import path
from .views import (Register,
                    Homepage,
                    Show_profile,
                    edit_profile)

app_name='authentication'

urlpatterns = [
    path('register/', Register, name='register'),
    path('homepage/', Homepage, name='homepage'),
    path('profile/', Show_profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit-profile'),
]