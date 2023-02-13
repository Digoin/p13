# Generated by Django 4.1.5 on 2023-02-01 14:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Adresse email'),
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ManyToManyField(related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]