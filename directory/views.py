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

        dictionary = {"lat": game.lat, "long": game.long, "when": str(game.when), "sport": game.sport, "open": game.isItOpen, "players_needed": game.players_needed, "skill_level": game.skill_level}

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

        #print(request.POST)

        sport = request.POST['sport_filter']

        skill = request.POST['skill_filter']

        print(sport)

        print(skill)

        a = games.objects.all().filter(sport = sport)

        if sport == "All" and skill == "All":

            gameList = games.objects.all()

        else:

            if skill == "All":

                gameList = games.objects.all().filter(sport = sport)

            elif sport == "All":

                gameList = games.objects.all().filter(skill_level = skill)

            else:

                gameList = games.objects.all().filter(sport = sport).filter(skill_level = skill)

        gameJSON = []
        
        for game in gameList:

            dictionary = {"lat": game.lat, "long": game.long, "when": str(game.when), "sport": game.sport, "open": game.isItOpen, "players_needed": game.players_needed, "skill_level": game.skill_level}
            
            gameJSON.append(dictionary)

        return HttpResponse(simplejson.dumps(gameJSON), content_type="application/json")
            

def signup(request):

    string = "blank"
    
    context = {
        string : "blank",
    }
    
    return render(request, "addgame.html", context)

def register(request):

    string = "null"

    return HttpResponse(string)
            

 

        
