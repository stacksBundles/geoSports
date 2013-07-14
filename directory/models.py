from django.db import models
from django.contrib.auth.models import User


class games(models.Model):

    lat = models.FloatField()

    long = models.FloatField()

    when = models.DateTimeField()

    sport = models.CharField(max_length = 140)

    isItOpen = models.BooleanField()

    players_needed = models.IntegerField(null = True)

    BEGINNER = "Beginner"

    COMPETITIVE = "Competitive"

    ELITE = "Elite"

    ALL = "All"

    SKILL_CHOICES = (
        (BEGINNER, "Beginner"),
        (COMPETITIVE, "Competitive"),
        (ELITE, "Elite"),
        (ALL, "All"),
        )

    skill_level = models.CharField(max_length = 11, choices = SKILL_CHOICES)


class locations(models.Model):

    TURF = "Turf"
    RINK = "Rink"
    TENNIS_COURT = "Tennis Court"
    SQUASH_COURT = "Squash Court"
    FIELD = "Field"
    BASKETBALL_COURT = "Basketball Court"

    LOCATION_TYPES = (
        (TURF, "Turf"),
        (RINK, "Rink"),
        (TENNIS_COURT, "Tennis Court"),
        (SQUASH_COURT, "Squash Court"),
        (FIELD, "Field"),
        (BASKETBALL_COURT, "Basketball Court"),
    )

    when = models.DateField()
    

class profile(models.Model):

    name = models.CharField(max_length = 140)

    sports_played = models.CharField(max_length = 500)

    reputation = models.IntegerField()

    


