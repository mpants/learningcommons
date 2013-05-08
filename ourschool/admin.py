'''
Created on Feb 5, 2013

@author: M.Charlemagne
'''
from django.contrib import admin
from ourschool.models import source, UserProfile

admin.site.register(source)
admin.site.register(UserProfile)