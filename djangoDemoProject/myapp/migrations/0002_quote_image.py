# Generated by Django 5.1.6 on 2025-02-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
