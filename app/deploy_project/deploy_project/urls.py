"""deploy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deploy_app import views
from deploy_app.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('<str:type>', views.credential_category),
    path('api/v1/', views.database),
    path('api/v1/People', views.people, name='list-people'),
    path('api/v1/People/<int:id>/', views.person),
    path('api/v1/Governments/', views.governments, name='list-governments'),
    path('api/v1/Governments/<int:id>/', views.government),
    path('api/v1/Enterprises/', views.enterprises, name='list-enterprises'),
    path('api/v1/Enterprises/<int:id>/', views.enterprise),
    path('api/v1/get', views.list),
    path('api/v1/post', views.entity),
    path('api/v1/add', views.add_item),
    path('api/v1/delete', views.delete_item),
]
