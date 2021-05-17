from django.db import models

# Create your models here.
class Employees2(models.Model):
    empid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employees2'

class Student(models.Model):
    s_id = models.IntegerField( blank=False)
    s_name = models.CharField(max_length=100)
    s_email = models.CharField(max_length=100)
    s_address = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'student'