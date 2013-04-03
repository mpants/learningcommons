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
  return render_to_response(t,c)

def test(request):
  return HttpResponse('Welcome to page %s' % request.path)


def home(request):
  #Home page
  if 'q' in request.GET and request.GET['q']:
    q = request.GET['q']
    sources = source.objects.filter(classtitle__icontains=q)
    return render_to_response('search_results.html', {'sources': sources, 'query': q})
  elif 'q' in request.GET and request.GET['q'] == '':
    classes = source.objects.all()
    c = RequestContext(request, {'classes':classes,'error':True})
    return render_to_response('home.html',c)
  else:
    classes = source.objects.all()
    c = RequestContext(request, {'classes':classes})
    return render_to_response('home.html',c)
  