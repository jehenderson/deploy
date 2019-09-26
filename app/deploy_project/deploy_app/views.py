from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from deploy_app.models import Person, Government, Enterprise
# Create your views here.

def hello(request):
  text = """<h1>welcome to my app !</h1>"""
  return HttpResponse(text)

def list(request, type):
  if (type == 'people'):
    item_list = Person.objects.order_by('pk')
    item_type = 'person'
  elif (type == 'governments'):
    item_list = Government.objects.order_by('pk')
    item_type = 'government'
  elif (type == 'enterprises'):
    item_list = Enterprise.objects.order_by('pk')
    item_type = 'enterprise'
  else:
    raise error
  template = loader.get_template('deploy_app/list.html')
  context = { 'item_list': item_list, 'item_type': item_type }
  return HttpResponse(template.render(context, request))

def item(request, type, item_id):
  if (type == 'person'):
    item = Person.objects.get(pk=item_id)
  elif (type == 'government'):
    item = Government.objects.get(pk=item_id)
  elif (type == 'enterprise'):
    item = Enterprise.objects.get(pk=item_id)
  else:
    raise error
  template = loader.get_template('deploy_app/entity.html')
  context = { 'item': item, 'item_id': item_id }
  return HttpResponse(template.render(context, request))

def add_item(request, type, id):
  pass

def update_item(request, type, id):
  pass

def delete_item(request, type, id):
  pass