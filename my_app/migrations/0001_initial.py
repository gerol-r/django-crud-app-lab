# Generated by Django 5.2.1 on 2025-05-31 21:34

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[('A', 'Action'), ('AD', 'Adventure'), ('AN', 'Anime'), ('ANT', 'Anthology'), ('C', 'Cartoon'), ('CO', 'Comedy'), ('COOK', 'Cooking Show'), ('CR', 'Crime'), ('D', 'Documentary'), ('DR', 'Drama'), ('E', 'Educational'), ('F', 'Fantasy'), ('G', 'Game Show'), ('H', 'Historical'), ('HO', 'Horror'), ('I', 'Infomercials'), ('L', 'Late Night'), ('M', 'Mockumentary'), ('MU', 'Music Television'), ('N', 'News Programming'), ('R', 'Reality TV'), ('RE', 'Religious'), ('RO', 'Romance'), ('S', 'Science Fiction'), ('SE', 'Serial'), ('SK', 'Sketch Comedy'), ('SO', 'Soap Opera'), ('SP', 'Sports'), ('T', 'Talk Shows'), ('V', 'Variety Shows'), ('W', 'Western'), ('SW', 'Space Western'), ('O', 'Other')], max_length=84)),
                ('streaming_platform', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('opinion', models.TextField()),
                ('date_watched', models.DateField(verbose_name='Date Watched')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='my_app.show')),
            ],
        ),
    ]
