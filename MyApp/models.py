from django.db import models
import uuid


class StudDetails(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_gender = models.CharField(max_length=10)
    stud_email = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=100)

class Team(models.Model):
    team_name = models.CharField(max_length=50)

class CricketPlayers(models.Model):    
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='team')
    country = models.CharField(max_length=50)

class VoterId(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
