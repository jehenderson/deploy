from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core import serializers
from deploy_app.models import *
import json

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

def upload_docs(request, type, id):
  return render(request, 'deploy_app/page3.html')

def list(request):
  people_list = Person.objects.all()
  entity_list = Enterprise.objects.all()
  governments = Government.objects.all()
  context = {"people": people_list, "entities": entity_list}
  return render(request, 'deploy_app/list.html', context)

def item(request):
  people = Person.objects.all()
  governments = Government.objects.all()
  enterprises = Enterprise.objects.all()
  template = loader.get_template('deploy_app/entity.html')
  context = {'people': people, 'governments': governments, 'enterprises': enterprises}
  return render(request, 'deploy_app/entity.html', context)

def add_item(request):

  return HttpResponseRedirect('')


def delete_item(request, type):
  if (type == 'person'):
    item = Person.objects.get(pk=item_id)
    item.delete()
  return HttpResponseRedirect('')
