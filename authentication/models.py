from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_pics', null=True,blank=True)
    full_name=models.CharField(max_length=100)
    is_mentor=models.BooleanField(default=False)
    is_mentee=models.BooleanField(default=False)
    education=models.CharField(max_length=100)
    skills=models.TextField()
    years_of_experience=models.PositiveIntegerField(default=0)
    mentorship_skills=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    

#slider

class slider (models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=800, blank=False)
    image= models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title  
