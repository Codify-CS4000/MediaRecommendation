# Generated by Django 2.2.2 on 2019-08-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20190804_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookseries',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
    ]