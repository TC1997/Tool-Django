from django.db import models

# Create your models here.
class Squirrel(models.Model):
    Longitude = models.CharField(max_length=30)
    Latitude = models.CharField(max_length=30)
    Unique_Squirrel_ID = models.CharField(max_length=30)
    Hectare = models.CharField(max_length=30)
    Shift = models.CharField(max_length=30)
    Date = models.DateField(blank=True)  # blank?
    Hectare_Squirrel_Number = models.CharField(max_length=30)
    Age = models.CharField(max_length=30, blank=True)
    Primary_Fur_Color = models.CharField(max_length=30, blank=True)
    Highlight_Fur_Color = models.TextField(blank=True)
    Combination_of_Primary_and_Highlight_Color = models.TextField(blank=True)
    Color_Notes = models.TextField(blank=True)
    Location = models.TextField(blank=True)
    Above_Ground_Sighter_Measurement = models.CharField(max_length=30, blank=True)
    Specific_Location = models.TextField(blank=True)
    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)
    Other_Activities = models.TextField(blank=True)
    Kuks = models.BooleanField(default=False)
    Quaas = models.BooleanField(default=False)
    Moans = models.BooleanField(default=False)
    Tail_Flags = models.BooleanField(default=False)
    Tail_Twitches = models.BooleanField(default=False)
    Approaches = models.BooleanField(default=False)
    Indifferent = models.BooleanField(default=False)
    Runs_From = models.BooleanField(default=False)
    Other_Interactions = models.TextField(blank=True)
    Lat_Long = models.TextField()
    Zip_Codes = models.CharField(max_length=30, blank=True)
    Community_Districts = models.CharField(max_length=30)
    Borough_Boundaries = models.CharField(max_length=30)
    City_Council_Districts = models.CharField(max_length=30)
    Police_Precincts = models.CharField(max_length=30)

    def __str__(self):
        return self.Unique_Squirrel_ID
