from django.contrib import admin
from .models import Category, Ebook, Review
# Register your models here.

admin.site.register(Category)
admin.site.register(Ebook)
admin.site.register(Review)