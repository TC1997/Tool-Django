from django.shortcuts import render
from django.http import HttpResponse
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

def list(request):
    squirrel_list = Squirrel.objects.all()
    context = {'squirrel_list': squirrel_list}
    return render(request, 'myApp/list.html', context)

def update(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(pk=unique_squirrel_id)
    if request.method == 'GET':
        form = SquirrelForm(instance=squirrel)
        return render(request, 'myApp/form.html', {'form': form})
    else:
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
        return redirect('/sightings')

def create(request):
    if request.method == 'GET':
        form = SquirrelForm1()
        return render(request, 'myApp/form1.html', {'form': form})
    else:
        form = SquirrelForm1(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings')

