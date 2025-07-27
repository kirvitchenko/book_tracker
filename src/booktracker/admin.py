from django.contrib import admin
from .models import Book, Author, Genre, Note
# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Note)