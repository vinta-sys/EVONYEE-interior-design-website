# Generated by Django 4.1.3 on 2023-01-23 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminend', '0004_workdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workdb',
            old_name='image',
            new_name='Image',
        ),
    ]