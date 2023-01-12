from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import Category, Ebook, Review 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('username','email')
        model=User

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('title','authors','cover_image','pdf','publisher','year')
        model=Ebook

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('name','description')
        model=Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('reviewer','ebook','note','rating')
        model=Review
