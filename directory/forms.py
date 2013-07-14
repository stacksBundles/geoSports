from django import forms
from django.forms import ModelForm
from directory.models import profile, games

class addGameForm(ModelForm):

    class Meta:

        model = games

        exclude = ('author', 'note')

##    lat = forms.FloatField()
##
##    long = forms.FloatField()
##
##    when = forms.DateField()
##
##    sport = forms.CharField()
##
##    isItOpen = forms.BooleanField()
##
##    players_needed = forms.IntegerField()
##
##    BEGINNER = "Beginner"
##
##    COMPETITIVE = "Competitive"
##
##    ELITE = "Elite"
##
##    LEVEL = "Any Level"
##
##    SKILL_CHOICES = (
##        (BEGINNER, "Beginner"),
##        (COMPETITIVE, "Competitive"),
##        (ELITE, "Elite"),
##        (LEVEL, 'Any Level'),
##        )
##
##    skill_level = forms.ChoiceField(choices = SKILL_CHOICES)

class filterForm(forms.Form):

    HOCKEY = "Hockey"
    SOCCER = "Soccer"
    FOOTBALL = "Football"
    RUGBY = "Rugby"
    TENNIS = "Tennis"
    BASEBALL = "Baseball"
    ULTIMATE = "Ultimate"
    VOLLEYBALL = "Volleyball"
    SQUASH = "Squash"
    
    SPORT = 'Any Sport'

    SPORT_CHOICES = (
        (SPORT, 'Any Sport'),
        (HOCKEY, "Hockey"),
        (SOCCER, "Soccer"),
        (FOOTBALL, "Football"),
        (RUGBY, "Rugby"),
        (TENNIS, "Tennis"),
        (BASEBALL, "Baseball"),
        (ULTIMATE, "Ultimate"),
        (VOLLEYBALL, "Volleyball"),
        
        )

    sport_filter = forms.ChoiceField(choices = SPORT_CHOICES)

    BEGINNER = "Beginner"
    COMPETITIVE = "Competitive"
    ELITE = "Elite"
    LEVEL = "Any Level"

    SKILL_CHOICES = (
        (LEVEL, 'Any Level'),
        (BEGINNER, "Beginner"),
        (COMPETITIVE, "Competitive"),
        (ELITE, "Elite"),
        
    )

    skill_filter = forms.ChoiceField(choices = SKILL_CHOICES)
            
class signupForm(forms.Form):

    class Meta:
        
        model = profile
    
    
