from django.contrib import admin

from .models import *

admin.site.register(CredentialType)
admin.site.register(CredentialRequirement)
admin.site.register(Document)
admin.site.register(Person)
admin.site.register(Government)
admin.site.register(Enterprise)
