from django.db import models

# Create your models here.

class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  def __str__(self):
    return self.first_name+" "+self.last_name
  
class Government(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Government_Citizens(models.Model):
  government_id = models.ForeignKey('Government', on_delete=models.CASCADE)
  person_id = models.ForeignKey('Person', on_delete=models.CASCADE)

class Enterprise(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Enterprise_Employees(models.Model):
  enterprise_id = models.ForeignKey('Enterprise', on_delete=models.CASCADE)
  person_id = models.ForeignKey('Person', on_delete=models.CASCADE)

class Enterprise_Customers(models.Model):
  enterprise_id = models.ForeignKey('Enterprise', on_delete=models.CASCADE)
  person_id =  models.ForeignKey('Person', on_delete=models.CASCADE)