from django.contrib.contenttypes import generic
from django.contrib.auth.models import User, Group
from django.db import models
from mezzanine.pages.models import Page, RichText
from mezzanine.core.models import Ownable
from hs_core.models import AbstractResource

#
# To create a new resource, use these three super-classes. 
#

class TestResource(Page, RichText, AbstractResource):
    resource_file = models.FileField(
        null=True,
        default='',
        upload_to='test_resource', # this will be the new folder under static/media off from the hydroshare2 dir
        help_text='This should be a text file.'
    )
    resource_description = models.TextField(
        null=False, blank=True,
        default='',
        help_text="Provide a description for this resource."
    )


