# Generated by Django 4.0.2 on 2022-02-19 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='upvotes'),
        ),
    ]