from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.

class Students(models.Model):
    regNo = models.IntegerField()
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    sirName = models.CharField(max_length=30)
    profileImage = models.ImageField(upload_to='images/', default=NULL)
    class Meta:
        db_table = "student"