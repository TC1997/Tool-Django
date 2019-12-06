from django.db import models

# Create your models here.
class Squirrel(models.Model):
    Longitude = models.CharField(max_length=30)
    Latitude = models.CharField(max_length=30)
    Unique_Squirrel_ID = models.CharField(max_length=30)
    Hectare = models.CharField(max_length=30)
    Shift = models.CharField(max_length=30)
    Date = models.DateField(blank=True)
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


    def __str__(self):
        return self.Unique_Squirrel_ID
