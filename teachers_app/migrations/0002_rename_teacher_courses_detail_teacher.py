# Generated by Django 4.2.5 on 2024-03-03 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_detail',
            old_name='Teacher',
            new_name='teacher',
        ),
    ]