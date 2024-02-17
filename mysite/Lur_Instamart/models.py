from django.db import models

# Create your models here.
class BOOKS(models.Model):
    book_image = models.CharField(max_length=1000)
    book_title = models.CharField(max_length=1000)
    author_name = models.CharField(max_length=1000)
    publish = models.CharField(max_length=1000)
    disc = models.CharField(max_length=1000)
    