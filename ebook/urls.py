from django.urls import path
from .views import CategoryViewSet, EbookViewSet, ReviewViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('users',UserViewSet, basename='users')
router.register('categories',CategoryViewSet, basename='categories')
router.register('reviews',ReviewViewSet, basename='reviews')
router.register('ebooks',EbookViewSet, basename='ebooks')
router.register('',EbookViewSet, basename='ebooks')
urlpatterns=router.urls
