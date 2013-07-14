from django import forms

class addGameForm(forms.Form):

    lat = forms.FloatField()

    long = forms.FloatField()

    when = forms.DateField()

    sport = forms.CharField()

    isItOpen = forms.BooleanField()

    players_needed = forms.IntegerField()

    BEGINNER = "Beginner"

    COMPETITIVE = "Competitive"

    ELITE = "Elite"

    ALL = "All"

    SKILL_CHOICES = (
        (BEGINNER, "Beginner"),
        (COMPETITIVE, "Competitive"),
        (ELITE, "Elite"),
        (ALL, 'All'),
        )

    skill_level = forms.ChoiceField(choices = SKILL_CHOICES)

    note = forms.CharField(max_length = 140)

class filterForm(forms.Form):

    HOCKEY = "Hockey"
    SOCCER = "Soccer"
    FOOTBALL = "Football"
    RUGBY = "Rugby"
    TENNIS = "Tennis"
    BASEBALL = "Baseball"
    ULTIMATE = "Ultimate"
    VOLLEYBALL = "Volleyball"
    ALL = 'All'

    SPORT_CHOICES = (
        (ALL, 'All'),
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
    ALL = "All"

    SKILL_CHOICES = (
        (ALL, 'All'),
        (BEGINNER, "Beginner"),
        (COMPETITIVE, "Competitive"),
        (ELITE, "Elite"),
        
    )

    skill_filter = forms.ChoiceField(choices = SKILL_CHOICES)
            

    
    
