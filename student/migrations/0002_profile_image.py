# Generated by Django 2.1 on 2020-04-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank='True', upload_to='profile_pics'),
        ),
    ]