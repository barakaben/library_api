from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
import datetime 
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=55)
    description=models.TextField()
    class Meta:
        verbose_name_plural="Categories"
    def __str__(self):   
        return self.name

class Ebook(models.Model):
    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year+1)]
    title=models.CharField(max_length=150)
    authors=models.CharField(max_length=150)
    publisher=models.CharField(max_length=150)
    cover_image=models.ImageField()
    pdf=models.FileField()
    category=models.ForeignKey(Category, on_delete=models.PROTECT, default=None)
    year = models.IntegerField(('year'),choices=YEAR_CHOICES,default=\
    datetime.datetime.now().year)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Rating(models.IntegerChoices):
        Bad=1
        Average=2
        Good=3
        Very_Good=4
        Excellent=5
    reviewer=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ebook=models.ForeignKey(Ebook, on_delete=models.CASCADE,default=None)
    note=models.TextField()
    rating=models.IntegerField(choices=Rating.choices)
    