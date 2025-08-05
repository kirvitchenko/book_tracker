from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.utils import timezone

class User(AbstractUser):
    """
    Модель пользователя которая наследуюется от Abstractuser
    """
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    book = models.ManyToManyField('booktracker.Book', through='users.UserBook')

    def __str__(self):
        return self.username

class UserBook(models.Model):
    """Модель которая используется для связи книги и пользователя:
    """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    book = models.ForeignKey('booktracker.Book', on_delete=models.CASCADE)
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