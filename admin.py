from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import TestResource
from hs_core.admin import GenericResourceAdmin

admin.site.register(TestResource, GenericResourceAdmin)
