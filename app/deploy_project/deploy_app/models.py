from django.db import models
import datetime
# Create your models here.

class CredentialType(models.Model):
    name = models.CharField(max_length=50)
    icon = models.URLField(null="true")
    complete = models.BooleanField()
    requirements = models.ManyToManyField("CredentialRequirement")

class Credential(models.Model):
    name = models.CharField(max_length=50)

class CredentialRequirement(models.Model):
    type = models.CharField(max_length=50)
    component_documents = models.ManyToManyField("Document")

class Document(models.Model):
    name = models.CharField(max_length=50)
    valid_from = models.DateField()
    valid_to = models.DateField()

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

class Enterprise(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self):
    return self.name
