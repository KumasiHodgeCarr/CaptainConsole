# Generated by Django 3.0.5 on 2020-05-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200513_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
