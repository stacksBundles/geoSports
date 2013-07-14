from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class games(models.Model):

    name = models.CharField(max_length = 140, null = True, default="Here")

    lat = models.FloatField()

    long = models.FloatField()

    when = models.DateTimeField()

    address = models.CharField(max_length = 140, default="default for testing, will be updated later")

    sport = models.CharField(max_length = 140)

    isItOpen = models.BooleanField()

    players_needed = models.IntegerField(null = True, default = 0)

    BEGINNER = "Beginner"

    COMPETITIVE = "Competitivxe"

    ELITE = "Elite"

    LEVEL = "Any Level"

    SKILL_CHOICES = (
        (BEGINNER, "Beginner"),
        (COMPETITIVE, "Competitive"),
        (ELITE, "Elite"),
        (LEVEL, "Any Level"),
        )

    skill_level = models.CharField(max_length = 11, choices = SKILL_CHOICES)

    note = models.CharField(max_length = 140, blank = True, default = "default for testing, will be updated later")

    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=1)
    


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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=1)


    


