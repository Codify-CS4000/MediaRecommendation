# Generated by Django 2.2.2 on 2019-07-10 16:15

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_auto_20190701_1600'),
        ('ratings', '0002_movieratinguser_predictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookratinguser',
            name='predictions',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='media.Book'),
        ),
        migrations.AlterField(
            model_name='bookratinguser',
            name='book_rating_ids',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='ordered_predictions', to='media.Book'),
        ),
        migrations.AlterField(
            model_name='movieratinguser',
            name='movie_rating_ids',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='media.Movie'),
        ),
    ]
