from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    teacher_or_student = models.BooleanField()
    instruments_played = models.TextField()
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Request(models.Model):
    name = models.CharField(max_length=100)
    teacher_or_student = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return self.name