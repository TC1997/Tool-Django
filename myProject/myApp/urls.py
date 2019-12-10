from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('sightings/', views.list, name='list'),
    path('sightings/add/', views.create, name='create'),  # note the sequence here
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<str:unique_squirrel_id>/', views.update, name='update'),
    path('sightings/<str:unique_squirrel_id>/delete', views.delete, name='delete'),
]
