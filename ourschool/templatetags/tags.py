'''
Include designed to check for current path so navigation can reflect 
current location.  hot stuff
'''

from django import template

register = template.Library()

#Registers this as a filter
@register.simple_tag
def active(request,pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

