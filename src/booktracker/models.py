from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Модель которая описывает книгу в системе
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ManyToManyField('booktracker.Author', verbose_name='Автор')
    genre = models.ManyToManyField('booktracker.Genre', verbose_name="Жанр")
    cover = models.ImageField(upload_to='\covers', blank=True, null=True, verbose_name='Обложка')

    def __str__(self):
        return self.title

class Author(models.Model):
    """
    Модель автора котоаря содержит только его имя
    """
    name = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Модель жанра котоаря содержит только его название
    """
    name = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.name


class Note(models.Model):
    """
    Модель заметки для книг
    """
    text = models.TextField()
    book = models.ForeignKey('booktracker.Book', on_delete=models.CASCADE)
    writing_datetime = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
