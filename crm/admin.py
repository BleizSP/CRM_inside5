from django.contrib import admin

# Register your models here.
from crm.models import Client, Operation, Status, Bank

admin.site.register(Client)
admin.site.register(Operation)
admin.site.register(Status)
admin.site.register(Bank)
