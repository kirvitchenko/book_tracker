from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField('Author')
    genre = models.ManyToManyField('Genre')
    start_reading_date = models.DateField(default=timezone.now)
    end_reading_date = models.DateField(default=timezone.now)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    text = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    writing_datetime = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
