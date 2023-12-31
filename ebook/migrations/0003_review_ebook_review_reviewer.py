# Generated by Django 4.1.5 on 2023-01-10 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebook', '0002_ebook_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ebook',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ebook.ebook'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
