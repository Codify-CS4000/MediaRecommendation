# Generated by Django 2.2.2 on 2019-07-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0008_auto_20190712_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('movies_count', models.IntegerField()),
                ('movies', models.ManyToManyField(to='media.Movie')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('books_count', models.IntegerField()),
                ('books', models.ManyToManyField(to='media.Book')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
