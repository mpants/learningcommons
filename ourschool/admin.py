'''
Created on Feb 5, 2013

@author: M.Charlemagne
'''
from django.contrib import admin
from ourschool.models import sources, users

admin.site.register(sources)
admin.site.register(users)