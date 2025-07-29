from django.contrib import admin
from .models import Book, Author, Genre, Note, User
# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Note)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'avatar']