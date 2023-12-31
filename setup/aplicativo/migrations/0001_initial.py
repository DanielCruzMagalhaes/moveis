# Generated by Django 4.2.5 on 2023-09-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='image')),
                ('icones', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Main2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='image')),
                ('icones', models.ImageField(upload_to='image')),
            ],
        ),
    ]
