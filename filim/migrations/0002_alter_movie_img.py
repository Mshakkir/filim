# Generated by Django 4.2.6 on 2024-03-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Img',
            field=models.ImageField(upload_to='img'),
        ),
    ]
