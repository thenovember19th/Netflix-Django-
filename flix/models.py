from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PasswordResetToken(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add = True)

MOVIE_TYPE=(
    ('single','single'),
    ('seasonal','seasonal')
)
AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)
class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created:str=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True)

    def __str__(self):
        return self.title
    

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')

    def __str__(self):
        return self.title