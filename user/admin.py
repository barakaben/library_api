from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class UserAdmn(UserAdmin):
    model =User
    list_display = ["email", "username",]

admin.site.register(User, UserAdmn)
