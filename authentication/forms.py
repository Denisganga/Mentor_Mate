from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Alumni,Student,School

class AlumniRegistrationForm(UserCreationForm):
    school=forms.ModelChoiceField(School.objects.all(), empty_label='select a school')
    graduation_year=forms.IntegerField(label='Graduation Year')
    bio=forms.CharField(widget=forms.Textarea(attrs={'rows':4}), required=False)
    course=forms.CharField(max_length=100, label='Area of study')

    class Meta:
        model=Alumni
        fields=[
            'school',
            'graduation_year',
            'bio',
            'course'
        ]

class StudentRegistrationForm(UserCreationForm):
    school=forms.ModelChoiceField(School.objects.all(), empty_label='select a school')
    registration_number=forms.CharField(max_length=50)
    course=forms.CharField(max_length=100, label='Area of study')

    class Meta:
        model=Student
        fields=[
            'school',
            'registration_number',
            'course'
        ]



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
        
