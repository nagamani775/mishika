# Generated by Django 2.1 on 2020-03-13 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]