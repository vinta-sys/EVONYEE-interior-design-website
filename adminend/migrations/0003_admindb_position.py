# Generated by Django 4.1.3 on 2023-01-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminend', '0002_wtwedodb'),
    ]

    operations = [
        migrations.AddField(
            model_name='admindb',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
