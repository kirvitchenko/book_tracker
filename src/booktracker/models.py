from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    """
    Модель пользователя которая наследуюется от Abstractuser и описывает дополниться поля:
    - avatar - аватар
    - bitrh_date - дату рождения
    - book - связь с моделью Book через модель UserBook
    """
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    book = models.ManyToManyField('Book', through='UserBook')

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    Модель которая описывает книгу в системе и содержит следующие поля:
    title - название
    author - автор
    genre = жанр
    """
    title = models.CharField(max_length=100)
    author = models.ManyToManyField('Author')
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title


class UserBook(models.Model):
    """Модель которая используется для связи книги и пользователся:
    user - пользователь по внешнему ключу
    book - по внешнему ключу
    start_ и end_reading_date - дата начала и окончания чтения
    rating - личная оценка пользователем книги от 1 до 10
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_reading_date = models.DateField(default=timezone.now)
    end_reading_date = models.DateField(default=timezone.now)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    class Meta:
        """
        Класс который предотвращает дублирование записей
        """
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book"], name="unique_user_book"
            )
        ]


class Author(models.Model):
    """
    Модель автора котоаря содержит только его имя
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Модель жанра котоаря содержит только его название
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    """
    Модель заметки которая содержит следующие поля
    text - сам текст заметки
    book - внешний ключ по которому замтека привязывается к книге
    writing_datetime - дата и время написания заметки
    last_edit_time - последняя редакция заметки
    """
    text = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    writing_datetime = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
