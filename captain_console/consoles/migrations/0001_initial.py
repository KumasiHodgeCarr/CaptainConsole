# Generated by Django 3.0.5 on 2020-05-05 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=999)),
                ('brand', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ConsolesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Consoles')),
            ],
        ),
        migrations.CreateModel(
            name='ConsolesMainImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consoles.Consoles')),
                ('image', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='consoles.ConsolesImage')),
            ],
        ),
    ]
