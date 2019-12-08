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

def delete(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(pk=unique_squirrel_id)
    squirrel.delete()
    return redirect('/sightings')

def stats(request):
    squirrel_list = Squirrel.objects.all()
    latitude_ = []
    longitude_ = []
    location_ = []
    other_activities_ = []
    primary_fur_color_ = []
    for squirrel in squirrel_list:
        latitude_.append(squirrel.Latitude)
        longitude_.append(squirrel.Longitude)
        location_.append(squirrel.Location)
        other_activities_.append(squirrel.Other_Activities)
        primary_fur_color_.append(squirrel.Primary_Fur_Color)
    MLati = '1'#np.mean(np.array(latitude_).astype(np.float))
    MLongi ='2' #np.mean(np.array(longitude_).astype(np.float))



    def count_(lst):
        return len([x for x in lst if x])

    NLoca = count_(location_)
    NOA = count_(other_activities_)
    NPFC = count_(primary_fur_color_)
    dict_ = {
        'Mean_of_Latitude': MLati,
        'Mean_of_Longitude': MLongi,
        'Count_of_Location': NLoca,
        'Count_of_Other_Activities': NOA,
        'Count_of_Primary_Fur_Color': NPFC
    }
    return render(request, 'myApp/stats.html', dict_)
