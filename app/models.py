from django.db import models

# # Create your models here.
# class User(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField(max_length=200)

class Tweet(models.Model):
    _id = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
    created_at = models.CharField(max_length=400)

