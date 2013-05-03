# Create your views her
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.template.defaultfilters import slugify
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
    
def viewlearning(request):
  #View a Learning's details
  learningrequest = request.path[14:]
  learning = source.objects.get(classurl__iexact=learningrequest)
  #learning = source.objects.get(classslug=learningrequest)
  return render_to_response('viewlearning.html',{'class':learning},RequestContext(request))
  
  
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
      return render_to_response('search_results.html', {'sources': sources, 'query': q}, RequestContext(request))
  #return home page, with or without errors
  classes = source.objects.all()
  likely = getLikely()
  never = getNever()
  suggestion = getSuggestion()
  c = RequestContext(request, {'classes':classes,'errors':errors,'suggestion':suggestion,'likely':likely,'never':never,})
  return render_to_response('home.html',c)

def getSuggestion():
  firstparts = ['Liturgical ','Cosmic ','Biodynamic ','Emergent ','Morphodynamic ','Cooperative ','Nonlinear ','Linear ','De','Homeodynamic ','Communitarian ','Dimensional ','Deconstructive ','Recombiant ','Diversifying ','Open source ','Backyard ','Synergetic ','Discordian ','Hyperaccelerated ','Entrepreneurial ','Dieuretical ','Dialectical ','Buddhist ','Post','Pre','Anti','Mythological ','Community ','Horticultural ','Permacultural ','Neo','Steampunk ','Non','Hierarchical ','Ethical ','Speculative ']
  secondparts = ['crystal ','fishing ','communication ','James Joyce ','swingset repair ','3D printing ','kitten ','website ','linear ','non','pre','post','anti','dimensional ','toroid ','bicycle ','crossfit ','arduino ','bird ','chicken ','bunny ','kickball ']
  thirdparts = ['dreaming','fishing','running','making','building','repairing','discourse','rhetorics','raising','tending','petting','cuddling','birthing','eating','walking','cycling','chilling','slacking','hiking','soldering','knitting','wiring','writing','poetry','thinking','visioning','sillyracing']
  return choice(firstparts) + choice(secondparts) + choice(thirdparts)

def getLikely():
  likelysee = ['Someone new to town making friends.','Curricula shared freely with other communities around the world.','Skills being taught that help meet real needs.','Pride in actual real-world accomplishments.','People discovering what they have to share.','Many ways to demonstrate competency in a skill.','As many formats of teaching as there are styles of learning.','Partnerships with towns, communities, and nonprofits.','A space for non-traditional subjects.','A wide range of economic backgrounds.','A parent studying to help their family.','Students learning in a sunlit park.','Students working on community projects.','People publishing work for the first time.','Forgotten thinkers and authors being celebrated.','Learning that grows across disciplines to create something new.',]
  return choice(likelysee)

def getNever():
  neversee = ['A building named after Fed Ex.','18 year olds gambling on disappearing jobs.','$150,000 of debt to get a degree.','Fake study programs to pass the football team.','Student research funded by the Department of Defense.','A bill in the mail.','20 years of debt.','A student launched into a career path they regret.','A false promise of jobs.','A class where students only show up for the exams.','The ups and downs of state education budgets.','A classroom of all twenty-somethings.','Someone turned away.','Partnerships with megacorporations','Trustees who own stock in student loan companies.',]
  return choice(neversee)