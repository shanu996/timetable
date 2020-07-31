from django.db import models
from django.contrib.auth.models import User

class Tables(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timetable = models.CharField(max_length=10000)
    def __str__(self):
        return self.timetable