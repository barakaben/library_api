from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets #IsAuthenticatedOrReadOnly
from .models import Category, Ebook, Review
from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, EbookSerializer, ReviewSerializer,\
    UserSerializer 
User=get_user_model()
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAdminOrReadOnly,)
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class EbookViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAdminOrReadOnly,)
    queryset=Ebook.objects.all()
    serializer_class=EbookSerializer    

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes=(IsAdminOrOwner)#objects.all()
    queryset=User.objects.all()                       
    serializer_class=UserSerializer
