# Generated by Django 2.2.2 on 2019-07-03 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_auto_20190703_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book_uid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='userauth.BookRatingUser'),
        ),
        migrations.AlterField(
            model_name='user',
            name='movie_uid',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='userauth.MovieRatingUser'),
        ),
    ]