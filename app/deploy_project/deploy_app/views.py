from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core import serializers
from deploy_app.models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def hello(request):
  credentials = CredentialType.objects.all()
  context = {"credentials": credentials}
  return render(request, 'deploy_app/home.html', context)

def credential_category(request, type):
  types = CredentialType.objects.all()
  credentials = Credential.objects.all()
  context = {"credentials": credentials, "types": types}
  return render(request, 'deploy_app/credential_category.html', context)

def list(request):
  people_list = Person.objects.all()
  entity_list = Enterprise.objects.all()
  governments = Government.objects.all()
  context = {"people": people_list, "entities": entity_list}
  return render(request, 'deploy_app/list.html', context)

def people(request):
  context = {"Type": "People", "listItem": Person.objects.all()}
  return render(request, 'deploy_app/list_item.html', context)

def governments(request):
  context = {"Type": "Governments", "listItem": Government.objects.all()}
  return render(request, 'deploy_app/list_item.html', context)

def enterprises(request):
  context = {"Type": "Enterprises", "listItem": Enterprise.objects.all()}
  return render(request, 'deploy_app/list_item.html', context)

def person(request, id):
  item = Person.objects.get(pk=id)

  person = item.first_name + " " + item.last_name
  dob = "Date of Birth: " + str(item.date_of_birth)

  return render(request, 'deploy_app/item.html', {"type": "People", "item":person, "other":dob})

def government(request, id):
  item = Government(name=gov)
  # dobField = Person._meta.get_field("date_of_birth")
  # dob = dobField.value_from_obj(person)
  name = getattr(item, "name")
  return render(request, 'deploy_app/item.html', {"type":"Governments", "item":name})

def enterprise(request, id):
  item = Enterprise(name=enter)
  # dobField = Person._meta.get_field("date_of_birth")
  # dob = dobField.value_from_obj(person)
  name = getattr(item, "name")
  return render(request, 'deploy_app/item.html', {"type":"Enterprises", "item":name})

def entity(request):
  people = Person.objects.all()
  governments = Government.objects.all()
  enterprises = Enterprise.objects.all()
  template = loader.get_template('deploy_app/entity.html')
  context = {'people': people, 'governments': governments, 'enterprises': enterprises}
  return render(request, 'deploy_app/entity.html', context)

def database(request):
  return render(request, 'deploy_app/database.html')

def add_item(request):

  return HttpResponseRedirect('')


def delete_item(request, type):
  if (type == 'person'):
    item = Person.objects.get(pk=item_id)
    item.delete()
  return HttpResponseRedirect('')

@csrf_exempt
def record_user(request):
    data = request.body.decode('utf-8')
    # This should create a post request and send data to the lambda function
    requests.post("https://lk6ocy6iqh.execute-api.us-east-1.amazonaws.com/default/analytics", data)
    # These 3 lines log to a text file
    # file1 = open("UserRecords.txt","a")
    # file1.write(response)
    # file1.close()
    return HttpResponseRedirect('')
    # return HttpResponse("test")
