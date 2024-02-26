from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

        fields=[
            'profile_picture',
            'full_name',
            'is_mentor',
            'is_mentee',
            'education',
            'skills',
            'years_of_experience',
            'mentorship_skills'
        ]
        
