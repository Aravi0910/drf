from django.db import models
import uuid


class StudDetails(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_gender = models.CharField(max_length=10)
    stud_email = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=100)

class Cricketers(models.Model):
    cricket_id = models.UUIDField(default=uuid.uuid3)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)