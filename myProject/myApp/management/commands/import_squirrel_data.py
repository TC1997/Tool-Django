import csv
import re
from django.core.management import BaseCommand
from myApp.models import Squirrel


class Command(BaseCommand):
    help = 'Load the squirrel csv file into the database'
    args = 'Data.csv'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                if reader.line_num == 1:
                    continue

                # define a function converting string to boolean
                def str_to_bool(str_):
                    return True if str.lower(str_) == 'true' else False

                # convert Date to date type
                match = re.search(r'(\d{2})(\d{2})(\d{4})', row[5])
                if match:
                    squirrel = Squirrel.objects.create(
                        Longitude=row[0],
                        Latitude=row[1],
                        Unique_Squirrel_ID=row[2],
                        Hectare=row[3],
                        Shift=row[4],
                        Date='-'.join([match.group(3), match.group(1), match.group(2)]),
                        Hectare_Squirrel_Number=row[6],
                        Age=row[7],
                        Primary_Fur_Color=row[8],
                        Highlight_Fur_Color=row[9],
                        Combination_of_Primary_and_Highlight_Color=row[10],
                        Color_Notes=row[11],
                        Location=row[12],
                        Above_Ground_Sighter_Measurement=row[13],
                        Specific_Location=row[14],
                        Running=str_to_bool(row[15]),
                        Chasing=str_to_bool(row[16]),
                        Climbing=str_to_bool(row[17]),
                        Eating=str_to_bool(row[18]),
                        Foraging=str_to_bool(row[19]),
                        Other_Activities=row[20],
                        Kuks=str_to_bool(row[21]),
                        Quaas=str_to_bool(row[22]),
                        Moans=str_to_bool(row[23]),
                        Tail_Flags=str_to_bool(row[24]),
                        Tail_Twitches=str_to_bool(row[25]),
                        Approaches=str_to_bool(row[26]),
                        Indifferent=str_to_bool(row[27]),
                        Runs_From=str_to_bool(row[28]),
                        Other_Interactions=row[29],
                        Lat_Long=row[30],
                        Zip_Codes=row[31],
                        Community_Districts=row[32],
                        Borough_Boundaries=row[33],
                        City_Council_Districts=row[34],
                        Police_Precincts=row[35],
                    )
