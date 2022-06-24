from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
# Register your models here.


from .models import *



TokenAdmin.raw_id_fields = ['user']
admin.site.register(APi_default)