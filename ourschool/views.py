# Create your views her
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from models import source

def display_meta_t(request):
  values = request.META.items()
  values.sort()
  test = 'Meta'
  c = Context({'values': values,'testvar':test})
  t = Template('{{ testvar }}<br/>{% for item in values %} {{ item }}<br/>{% endfor %}')
  return HttpResponse(t.render(c))

def home(request):
  #Home page
  classes = source.objects.all()
  c = RequestContext(request, {'classes':classes})
  return render_to_response('home.html',c)
  