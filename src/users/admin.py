from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserBook

admin.site.register(UserBook)
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'avatar']
# Register your models here.
