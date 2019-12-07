from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import SquirrelForm, SquirrelForm1
import numpy as np

from .models import Squirrel


def map(request):
    sightings0 = Squirrel.objects.all()
    # sightings = sightings0[:10]
    sightings_loc_ = []
    sightings = []
    for i in range(120):
        sightings_loc = [sightings0[i].Latitude, sightings0[i].Longitude]
        if sightings_loc not in sightings_loc_:
            sightings_loc_.append(sightings_loc)
            sightings.append(sightings0[i])
        if len(sightings) == 100:
            break
    context = {'sightings': sightings}
    return render(request, 'myApp/map.html', context)
