from django.contrib import admin
from .models import Devices

models_list = [Devices]
admin.site.register(models_list)