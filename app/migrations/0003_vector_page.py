# Generated by Django 3.2.25 on 2024-10-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='vector_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('tags', models.TextField(blank=True)),
                ('img', models.FileField(upload_to='pic/%Y/%m/%d')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]