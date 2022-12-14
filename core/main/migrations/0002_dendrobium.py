# Generated by Django 4.1 on 2022-08-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dendrobium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Dendrobium name')),
                ('about', models.TextField(verbose_name='Dendrobium about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Dendrobium image')),
            ],
        ),
    ]
