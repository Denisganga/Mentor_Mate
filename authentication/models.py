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

class School(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Alumni(models.Model):
    user=models.OneToOneField(User,on_delete= models.CASCADE) #many mentorship instances can be associated with one alumni
    school=models.ForeignKey(School,on_delete=models.CASCADE) #one alumni can be associated with only one school, but a school can have many alumnis
    graduation_year=models.PositiveIntegerField()
    bio=models.TextField(blank=True)
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    user=models.OneToOneField(User,on_delete= models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=50) 
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

 #Tuples are used to store multiple items in a single variable   
MENTORSHIP_STATUS_CHOICES=(
    ('P','Pending'),
    ('A','Active'),
    ('C','Completed')
)
    
class Mentorship(models.Model):
    mentor = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='mentorship_mentor')
    mentee = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='mentorship_mentee')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=MENTORSHIP_STATUS_CHOICES)

    def __str__(self):
        return f'{self.mentor.user.username} mentoring {self.mentee.user.username}'



    

