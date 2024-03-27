# Generated by Django 4.2.6 on 2024-03-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('Img', models.ImageField(upload_to='gallery')),
                ('category', models.CharField(max_length=100)),
                ('trailer_link', models.URLField()),
            ],
        ),
    ]
