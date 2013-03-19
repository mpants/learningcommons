# Create your views her
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.shortcuts import render_to_response
from models import source

def display_meta_t(request):
  values = request.META.items()
  values.sort()
  test = 'Meta'
  c = Context({'values': values,'testvar':test})
  t = Template('{{ testvar }}<br/>{% for item in values %} {{ item }}<br/>{% endfor %}')
  return HttpResponse(t.render(c))

def display_classes(request):
  classes = source.objects.all()
  return render_to_response('displayclasses.html',{'classes':classes})
  