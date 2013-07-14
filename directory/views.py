# Create your views here.
from django.shortcuts import render, redirect
from directory.forms import addGameForm, filterForm
from directory.models import games, locations, profile
from django.utils import simplejson
import re

def index(request):

    gameList = games.objects.all()

    gameJSON = []

    for game in gameList:

        date = str(game.when)

        numbers = re.findall("(\d+)", date)

        newDate = ""
        
        for bits in numbers:

            newDate = newDate + bits + "/"

        newDate = newDate[:-1]

        dictionary = {"lat": game.lat, "long": game.long, "when": newDate, "sport": game.sport, "open": game.isItOpen}

        entry = simplejson.dumps(dictionary)

        gameJSON.append(entry)
    

    form = filterForm()

    if form:

        print("form passed" + str(type(form)))

    context = {
        "gameList": gameJSON,
        "form": form,
        }

    return render(request, "index.html", context)

def addGame(request):

    if request.is_ajax():

        form = addGameForm()

        context = {
            "form": form,
            }

        return render(request, "addGame.html", context)
        


def submitGame(request):

    if request.method == "POST" and request.is_ajax():

        data = {}

        data['lat'] = request.POST['lat']

        data['long'] = request.POST['long']

        data['when'] = request.POST['when']

        data['sport'] = request.POST['sport']

        data['isItOpen'] = request.POST['open']

        if not request.POST['open']:

            data['players_needed'] = request.POST['players']

        data['skill_level'] = request.POST['skill']

        validate = addGameForm(data)

        if validate.is_valid():
            
            new_game = games.objects.create(lat = data['lat'], long = data['long'], when = data['when'], sport = data['sport'], isItOpen = data['isItOpen'], players_needed = data['players_needed'], skill_level = data['skill_level'])

            new_game.save()

            gameList = games.objects.all()

            justPosted = new_game

            statusReturn = "Null"

            context = {
                "statusReturn": statusReturn,
                "gameList": gameList,
                "justPosted": justPosted,
                }

            return render(request, "index.html", context)

        else:

            statusReturn = "Game save failed"

            gameList = games.objects.all()

            context = {
                "statusReturn": statusReturn,
                "gameList": gameList,
                }

            return render(request, "index.html", context)


    
def signup(request):

    string = "Null"

    context = {
        "string": string,
        }

    return render(request, "signup.html", context)
        
def filter(request):

    if request.is_ajax():

        print("AJAX BABY")

        sport = request.POST['sport']

        if sport == "All":

            gameList = games.objects.all().filter(skill_level = request.POST['skill_level'])

        else:

            gameList = games.objects.all().filter(sport = sport, skill_level = request.POST['skill_level'])

        if not gameList:

            statusReturn = "Sorry, no one is playing " + str(sport) + ", how about you start a game?"

            gameList = games.objects.all()

            return render(request, "updatedMap.html", context)

        statusReturn = "Filtered by sport type: " + str(sport) + " and skill level: " + str(skill_level)

        context = {
            "gameList": gameList,
            "statusReturn": statusReturn,
            }

        return render(request, "updatedMap.html", context)
            

 
            

 

        
