from django.db import models

# Create your models here.

class Profile(models.Model):
    profileid = models.IntegerField()
    name      = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'profile'