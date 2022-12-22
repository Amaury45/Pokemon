from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/<int:id>/', views.pokemon, name='pokemon'),
    path('ability/<int:id>/', views.ability, name='ability'),
    path('name/', views.name, name='name'),
    path('team/', views.team, name='team'),
    path('setTeam/<int:id>', views.setTeam, name='setTeam'),
    path('', views.index, name='index'),
    path('en', views.index, name='index'),
    path('type', views.type, name='type')
]
