from django.contrib import admin

from .models import Person, Government, Government_Citizens, Enterprise, Enterprise_Employees, Enterprise_Customers

admin.site.register(Person)
admin.site.register(Government)
admin.site.register(Government_Citizens)
admin.site.register(Enterprise)
admin.site.register(Enterprise_Employees)
admin.site.register(Enterprise_Customers)

