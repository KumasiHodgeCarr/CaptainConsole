# Generated by Django 3.0.5 on 2020-05-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captain_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slideImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(blank=True, max_length=255)),
                ('Description', models.CharField(blank=True, max_length=500)),
                ('image', models.CharField(blank=True, max_length=999)),
            ],
        ),
        migrations.DeleteModel(
            name='slides',
        ),
    ]
