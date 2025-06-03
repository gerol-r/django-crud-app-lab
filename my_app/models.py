from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
GENRE_CHOICES = [
    ("A", "Action"),
    ("AD", "Adventure"),
    ("AN", "Anime"),
    ("ANT", "Anthology"),
    ("C", "Cartoon"),
    ("CO", "Comedy"),
    ("COOK", "Cooking Show"),
    ("CR", "Crime"),
    ("D", "Documentary"),
    ("DR", "Drama"),
    ("E", "Educational"),
    ("F", "Fantasy"),
    ("G", "Game Show"),
    ("H", "Historical"),
    ("HO", "Horror"),
    ("I", "Infomercials"),
    ("L", "Late Night"),
    ("M", "Mockumentary"),
    ("MU", "Music Television"),
    ("N", "News Programming"),
    ("R", "Reality TV"),
    ("RE", "Religious"),
    ("RO", "Romance"),
    ("S", "Science Fiction"),
    ("SE", "Serial"),
    ("SK", "Sketch Comedy"),
    ("SO", "Soap Opera"),
    ("SP", "Sports"),
    ("T", "Talk Shows"),
    ("V", "Variety Shows"),
    ("W", "Western"),
    ("SW", "Space Western"),
    ("O", "Other"),
]

class Show(models.Model):
    title = models.CharField(max_length=200)
    genres = MultiSelectField(choices=GENRE_CHOICES)  # Allows multi-select vice multiple choice
    streaming_platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

class Review(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 scale
    opinion = models.TextField()
    date_watched = models.DateField('Date Watched')

    def __str__(self):
        return f"Review for {self.show.title} ({self.rating}/5)"