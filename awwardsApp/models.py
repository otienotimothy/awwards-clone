from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image')
    bio = models.TextField(null=True, blank=True)
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    projectUrl = models.CharField(max_length=200)
    

class Rating(models.Model):
    design = models.IntegerField(min=1, max=10, default=5)
    usability = models.IntegerField(min=1, max=10, default=5)
    content = models.IntegerField(min=1, max=10, default=5)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_rating')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
