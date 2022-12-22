import contextvars

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from .forms import SearchForm
import random

import json

from . import models
from .models import Pokemon

pokemonTeam = []
allPokemon = []

def team(request):
    context = {}
    listPoke = []
    listPokeAdv = []
    size = [0,0,0,0,0,0]
    for x in range(0, len(size)):
        j = random.randint(1, 1000)
        infoPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(j) + '/').json()
        #infoPokeFr = requests.get('https://pokebuildapi.fr/api/v1/pokemon/' + str(j) + '/').json()
        i = random.randint(1, 1000)
        infoPokeAdv = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i) + '/').json()
        poke = models.Pokemon(infoPoke['id'], infoPoke['name'], infoPoke['sprites']['front_shiny'])
        pokeAdv = models.Pokemon(infoPokeAdv['id'], infoPokeAdv['name'], infoPokeAdv['sprites']['front_shiny'])
        for y in range(0, len(infoPoke['abilities'])):
            poke.addAbility(
                models.Ability(getAbilityId(infoPoke['abilities'][y]['ability']['url']),
                               infoPoke['abilities'][y]['ability']['name']))
        for z in range(0, len(infoPokeAdv['abilities'])):
            pokeAdv.addAbility(
                models.Ability(getAbilityId(infoPokeAdv['abilities'][z]['ability']['url']),
                               infoPokeAdv['abilities'][z]['ability']['name']))
        listPoke.append(poke)
        listPokeAdv.append(pokeAdv)
        context = {
            'listPoke': listPoke,
            'listPokeAdv': listPokeAdv
        }
    return render(request, 'team.html', context)

def pokemon(request, id: int):
    infoPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(id) + '/').json()
    poke = models.Pokemon(infoPoke['id'], infoPoke['name'], infoPoke['sprites']['front_shiny'])
    for y in range(0, len(infoPoke['abilities'])):
        poke.addAbility(
            models.Ability(getAbilityId(infoPoke['abilities'][y]['ability']['url']),
                           infoPoke['abilities'][y]['ability']['name'])
        )
    context = {'poke': poke}
    return render(request, 'pokemon.html', context)





def name(request):
    return index(request)




def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            infoPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(form.data['your_name'])).json()
            poke = models.Pokemon(infoPoke['id'], infoPoke['name'], infoPoke['sprites']['front_shiny'])
            return pokemon(request, poke.id)

    else:
        global allPokemon
        if not allPokemon:
            listPoke = setList()
            allPokemon = listPoke
            print("Not all Poke en")
        else:
            listPoke = allPokemon
            print("All Poke EN")


        form = SearchForm()
        context = {'listPoke': listPoke,
                   'form': form}
        return render(request, 'index.html', context)




def ability(request, id: int):
    infoAbi = requests.get('https://pokeapi.co/api/v2/ability/' + str(id) + '/').json()
    abi = models.Ability(infoAbi['id'], infoAbi['name'])
    abi.effect = infoAbi['effect_entries'][1]['effect']
    context = {'ability': abi}
    return render(request, 'ability.html', context)

def type(request):
    infoType = requests.get('https://pokebuildapi.fr/api/v1/types').json()
    type = models.Type("null", "null")
    infoPoke = requests.get('https://pokebuildapi.fr/api/v1/pokemon/').json()
    listType = models.listType(1)
    for y in range(0, len(infoPoke)):
        for b in range(0, len(infoPoke[y]['apiTypes'])):
            if infoPoke[y]['apiTypes'][b]['name'] == "Plante":
                listType.addPlante(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Feu":
                listType.addFeu(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Eau":
                listType.addEau(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Sol":
                listType.addSol(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Vol":
                listType.addVol(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Dragon":
                listType.addDragon(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Psy":
                listType.addPsy(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Fée":
                listType.addFee(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Ténèbres":
                listType.addTenebre(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Acier":
                listType.addAcier(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Glace":
                listType.addGlace(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Roche":
                listType.addRoche(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Spectre":
                listType.addSpectre(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Combat":
                listType.addCombat(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Normal":
                listType.addNormal(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Électrik":
                listType.addElek(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Insecte":
                listType.addInsecte(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )
            if infoPoke[y]['apiTypes'][b]['name'] == "Poison":
                listType.addPoison(
                    models.Pokemon(infoPoke[y]['id'], infoPoke[y]['name'], infoPoke[y]['image'])
                )

    for x in range(0, len(infoType)):
        type.addType(
            models.Type(infoType[x]['name'], infoType[x]['image'])
        )

    context = {'type': type,
               'list': listType}
    return render(request, 'type.html', context)
def setList():
    finalList = []
    ListPokemon = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151').json()['results']

    for x in range(0, len(ListPokemon)):
        pokemonInfo = requests.get(ListPokemon[x]["url"]).json()
        finalList.append(
            models.Pokemon(pokemonInfo['id'], pokemonInfo['name'], pokemonInfo['sprites']['front_shiny']))
        for y in range(0, len(pokemonInfo['abilities'])):
            finalList[x].addAbility(
                models.Ability(getAbilityId(pokemonInfo['abilities'][y]['ability']['url']),
                               pokemonInfo['abilities'][y]['ability']['name'])
            )
    return finalList


    for x in range(0, len(ListPokemon)):
        i = random.randint(1, 1000)
        randomPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(ListPokemon[x]['id']) + '/').json()
        #pokemonInfo = requests.get(ListPokemon[x])
        finalList_fr.append(
            models.PokemonS(ListPokemon[x]['id'], ListPokemon[x]['name'], ListPokemon[x]['sprite'], i, randomPoke['sprites']['front_shiny']))
    return finalList_fr


def getAbilityId(url):
    return requests.get(url).json()['id']




def setTeam(request, id):
    pokemonTeam.append(id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
