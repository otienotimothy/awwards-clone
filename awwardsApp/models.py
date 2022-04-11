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
    projectUrl = models.URLField(max_length=200)
    projectBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='projects')
    

class Rating(models.Model):
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_rating')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
