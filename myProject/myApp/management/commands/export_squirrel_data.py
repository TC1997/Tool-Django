import csv
import re
from django.core.management import BaseCommand
from myApp.models import Squirrel


class Command(BaseCommand):
    help = 'Export the squirrel data into a csv file'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'w') as f:
            writer = csv.writer(f, dialect='excel')
            row = ['Longitude', 'Latitude', 'Unique_Squirrel_ID', 'Hectare', 'Shift', 'Date', 'Hectare_Squirrel_Number',
                   'Age', 'Primary_Fur_Color', 'Highlight_Fur_Color', 'Combination_of_Primary_and_Highlight_Color',
                   'Color_Notes', 'Location', 'Above_Ground_Sighter_Measurement', 'Specific_Location',
                   'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other_Activities',
                   'Kuks', 'Quaas', 'Moans', 'Tail_Flags', 'Tail_Twitches', 'Approaches', 'Indifferent', 'Runs_From',
                   'Other_Interactions', 'Lat_Long', 'Zip_Codes', 'Community_Districts',
                   'Borough_Boundaries', 'City_Council_Districts', 'Police_Precincts']
            writer.writerow(row)
            for squirrel in Squirrel.objects.all():
                row = [
                    squirrel.Longitude,
                    squirrel.Latitude,
                    squirrel.Unique_Squirrel_ID,
                    squirrel.Hectare,
                    squirrel.Shift,
                    squirrel.Date,
                    squirrel.Hectare_Squirrel_Number,
                    squirrel.Age,
                    squirrel.Primary_Fur_Color,
                    squirrel.Highlight_Fur_Color,
                    squirrel.Combination_of_Primary_and_Highlight_Color,
                    squirrel.Color_Notes,
                    squirrel.Location,
                    squirrel.Above_Ground_Sighter_Measurement,
                    squirrel.Specific_Location,
                    squirrel.Running,
                    squirrel.Chasing,
                    squirrel.Climbing,
                    squirrel.Eating,
                    squirrel.Foraging,
                    squirrel.Other_Activities,
                    squirrel.Kuks,
                    squirrel.Quaas,
                    squirrel.Moans,
                    squirrel.Tail_Flags,
                    squirrel.Tail_Twitches,
                    squirrel.Approaches,
                    squirrel.Indifferent,
                    squirrel.Runs_From,
                    squirrel.Other_Interactions,
                    squirrel.Lat_Long,
                    squirrel.Zip_Codes,
                    squirrel.Community_Districts,
                    squirrel.Borough_Boundaries,
                    squirrel.City_Council_Districts,
                    squirrel.Police_Precincts,
                ]
                writer.writerow(row)




