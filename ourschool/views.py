# Create your views her
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.shortcuts import render_to_response
from models import source
from forms import addlearning, sourceform
from random import choice

def display_meta_t(request):
  values = request.META.items()
  values.sort()
  test = 'Meta'
  c = Context({'values': values,'testvar':test})
  t = Template('{{ testvar }}<br/>{% for item in values %} {{ item }}<br/>{% endfor %}')
  return render_to_response(t,c)

def test(request):
  return HttpResponse('Welcome to page %s' % request.path)

def submitted(request):
  return HttpResponse('Your local learning is submitted.  After making sure it\'s not unusually illegal, morally repressive, or a seminar on Ayn Rand, we\'ll get it up on the site!')

def submitlearning(request):
  if request.method == 'POST':
    #form = addlearning(request.POST)
    form = sourceform(request.POST)
    if form.is_valid():
      cleaned = form.cleaned_data
      '''
      send_mail(
        cd['title'],
        cd['subject'],
        cd['format'],
        cd['host'],
        cd['date'],
        ['nostickgnostic@gmail.com'],
      )
      '''
      #save a new source from the form's data
      new_source = form.save()
      
      return HttpResponseRedirect('/submittedlearning/')
  else:
    form = sourceform(initial={'host': 'Community Member'})
  return render_to_response('submitlearning.html', {'form': form}, RequestContext(request))
    

def home(request):
  #Home page
  errors = []
  if 'q' in request.GET:
    #search query
    q = request.GET['q']
    if not q:
      errors.append('Enter a search term')
    elif len(q) > 12:
      errors.append('Too long of a search')
    else:
      #render search results page
      sources = source.objects.filter(classtitle__icontains=q)
      return render_to_response('search_results.html', {'sources': sources, 'query': q})
  #return home page, with or without errors
  classes = source.objects.all()
  suggestion = getSuggestion()
  c = RequestContext(request, {'classes':classes,'errors':errors,'suggestion':suggestion})
  return render_to_response('home.html',c)

def getSuggestion():
  firstparts = ['Liturgical ','Cosmic ','Biodynamic ','Emergent ','Morphodynamic ','Cooperative ','Nonlinear ','Linear ','De','Homeodynamic ','Communitarian ','Dimensional ','Deconstructive ','Recombiant ','Diversifying ','Open source ','Backyard ','Synergetic ','Discordian ','Hyperaccelerated ','Entrepreneurial ','Dieuretical ','Dialectical ','Buddhist ','Post','Pre','Anti','Mythological ','Community ','Horticultural ','Permacultural ','Neo','Steampunk ','Non','Hierarchical ','Ethical ','Speculative ']
  secondparts = ['crystal ','fishing ','communication ','James Joyce ','swingset repair ','3D printing ','kitten ','website ','linear ','non','pre','post','anti','dimensional ','toroid ','bicycle ','crossfit ','arduino ','bird ','chicken ','bunny ','kickball ']
  thirdparts = ['dreaming','fishing','running','making','building','repairing','discourse','rhetorics','raising','tending','petting','cuddling','birthing','eating','walking','cycling','chilling','slacking','hiking','soldering','knitting','wiring','writing','poetry','thinking','visioning','sillyracing']
  return choice(firstparts) + choice(secondparts) + choice(thirdparts)