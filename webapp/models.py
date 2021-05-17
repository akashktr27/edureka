from django.db import models


# Create your models here.

class Employees(models.Model):
    empid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employees'


class Login_users(models.Model):
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Users_data'
