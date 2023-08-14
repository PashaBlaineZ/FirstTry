# Generated by Django 4.2.3 on 2023-08-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=20, verbose_name='Автор')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('amount', models.CharField(max_length=5, verbose_name='Количество')),
            ],
        ),
    ]
