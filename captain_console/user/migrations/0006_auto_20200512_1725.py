# Generated by Django 3.0.5 on 2020-05-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200512_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='../static/images/avatar.png', upload_to=''),
        ),
    ]
