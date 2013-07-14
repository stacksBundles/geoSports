# Create your views here.
from django.shortcuts import render, redirect
from directory.forms import addGameForm, filterForm
from directory.models import games, locations, profile
from django.utils import simplejson
import re
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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

        dictionary = {"lat": game.lat, "long": game.long, "when": newDate, "sport": game.sport, "open": game.isItOpen, "players_needed": game.players_needed, "skill_level": game.skill_level}

        entry = simplejson.dumps(dictionary)

        gameJSON.append(entry)
    

    form = filterForm()

    context = {
        "gameList": gameJSON,
        "form": form,
        }

    return render(request, "index.html", context)

def addGame(request):

    if request.is_ajax():

        form = addGameForm()

        context = {
            "statusUpdate": statusUpdate,
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

        else:

            data['players_needed'] = ""

        data['skill_level'] = request.POST['skill']

        validate = addGameForm(data)

        if validate.is_valid():
            
            new_game = validate.save()

            gameList = games.objects.all()

            justPosted = new_game

            response = HttpResponse("success")

            return response

        else:

            response = HttpResponse("failure")

            return response


def register(request):

    if request.method == "POST" and request.is_ajax():

        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            new_user = form.save()
            
            return HttpResponse("success")
        
    else:
        
        form = UserCreationForm()

        context = {
            "form": form,
            }
        
    return render(request, "registration/register.html", context)
        
def filter(request):

    if request.is_ajax():

        print("AJAX BABY")

        sport = request.POST['sport_filter']

        skill = request.POST['skill_filter']

        if sport == "All":

            gameList = games.objects.all().filter(skill_level = request.POST['skill_filter'])

        elif skill == "All":

            gameList = games.objects.all().filter(sport = sport, skill_level = request.POST['skill_filter'])

        if not gameList:

            statusReturn = "Sorry, no one is playing " + str(sport) + ", how about you start a game?"

            return HttpResponse(statusReturn)

        return HttpResponse(gameList)
            

def signup(request):

    string = "blank"
    
    context = {
        string : "blank"
    }
    
    return render(request, "signup.html", context)
            

 

        
