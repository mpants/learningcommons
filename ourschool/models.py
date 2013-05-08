from django.db import models
from django.template.defaultfilters import slugify
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class source(models.Model):
  #source of learning - to populate available classes. flexible enough for many formats
  
  #Possible class statuses
  STATUS_CHOICES = (
                    ('active','Active Now'),
                    ('proposed','Proposed'),
                    ('finished','Finished'),
                    ('canceled','Canceled'),
                    ('starting','Starting Soon'),
                    
                    
                    )
  
  #Possible class formats
  FORMAT_CHOICES = (
                    ('colearn','Co-Learn'),
                    ('handson','Hands-On'),
                    ('seminar','Seminar'),
                    ('lecture','Lecture'),
                    ('discussion','Discussion'),
                    ('bookclub','Book Club'),
                    ('project','Project'),
                    ('dit','Do It Together'),
                    ('conversation','Conversation'),
                    ('story','Storytelling'),
                    ('collaboration','Collaboration'),
                    ('apprenticeship','Apprenticeship'),
                    ('mentoring','Mentoring'),
                    ('demonstration','Demonstration'),
                    ('skillshare','Skillshare / Skilltrade'),
                    ('freeform','Freeform'),
                    ('competition','Competition'),
                    ('game','Game Learning'),
                    ('localmedia','Local Media'),
                    ('volunteering','Volunteering'),
                    ('other','Other'),
                    ('intensive','Intensive'),                    
                    )
  

  classtitle = models.CharField(max_length='70',verbose_name='Title',unique=True,help_text='example: Learn Permacultural Approaches To Oral Hygeine / Bicycles!')
  #title of class
  #classslug = AutoSlugField(max_length=50, unique=True, populate_from=('classtitle',))
  #class slug
  classdescription = models.TextField(verbose_name='Description',help_text='Write about your relevant experience (if any!), learning goals for yourself and others.  Also include prerequisites, materials costs, and anything else unique.')
  #description of class
  classstatus = models.CharField(max_length='30',blank=True,verbose_name='Status',choices=STATUS_CHOICES)
  #does the class exist, is it finished, or is it only proposed?
  classsubject = models.CharField(max_length='30',blank=True,verbose_name='Subject',help_text='Broad subject, i.e.: Philosophy')
  #broad subject, i.e. programming
  classformat = models.CharField(max_length='40',blank=True,verbose_name='Format',choices=FORMAT_CHOICES,help_text='See help for format explanations')
  #format of class, i.e. lecture
  classhost = models.CharField(max_length='50',blank=True,verbose_name='Host',help_text='Teacher, Facilitator, Organization, or Host of class')
  #who teaches or initiates it, i.e. community member, communecos, etc  
  classstartdate = models.DateField(blank=True,verbose_name='Start Date',help_text='First Learning Date')
  #start date
  classnextdate = models.DateField(blank=True,verbose_name='Next Date',help_text='Next Date of Activity')
  #next date
  classfrequency = models.CharField(max_length='40',verbose_name='Frequency',help_text='i.e. Weekly, One Time, Daily, etc.')
  classcost = models.CharField(max_length='40',blank=True,verbose_name='Cost?',default='Free',help_text='Most should be free.  Others accept money, IOUs, barter, work trade, food, etc.!')
  #free, ious, villages, $30, etc.
  classaccredited = models.BooleanField(blank=True,verbose_name='Accredited?',help_text='Whether or not you (informally) offer recognition of work done by others in this context, even if they are your peers.')
  #is some kind of credit given?
  classsite = models.URLField(blank=True,verbose_name='Info Website',help_text='Website with info about the class')
  #url for more info
  classgroupurl = models.URLField(blank=True,verbose_name='Resource Website',help_text='Website for a class google group, wiki, etc.')
  #url for a google group, wiki, etc.
  classemail = models.EmailField(blank=True,verbose_name='Host Email',help_text='Contact Email For the Learning')
  #email of instructor or organization
  classusers = models.ManyToManyField('UserProfile',related_name='participants',blank=True)
  #users participating in a class
  classinterested = models.ManyToManyField('UserProfile',related_name='interested',blank=True)
  #users interested in a class
  classcertified = models.ManyToManyField('UserProfile',related_name='certified',blank=True)
  #users certified in a class
  classteachers = models.ManyToManyField('UserProfile',related_name='teachers',blank=True)
  #teacher of class user model
  classtown= models.CharField(max_length='40',verbose_name='City',blank=True)
  classlocation = models.TextField(blank=True,verbose_name='Location')
  #where the class is taking place
  classphoto = models.ImageField(blank=True,verbose_name='Image',upload_to='media/classphotos/')
  #image for class
  classrelated = models.ManyToManyField('self',blank=True,verbose_name='Related Classes')
  #related classes
  classurl = AutoSlugField(populate_from='classtitle')
  
  
  def _get_password(self):
    password = User.objects.make_random_password()
    return password
    
  #password to edit class
  classpass = _get_password
  
  def _get_fields(self):
    return [(field.name, field.value_to_string(self)) for field in source._meta.fields]
  
  #def _get_url(self):
    #makes URL from class title
  #  return slugify(self.classtitle)
  
  #classurl = property(_get_url)
  
  def _get_num_users(self):
    #Gets number of users
    return len(self.classusers)
  
  classnumusers = property(_get_num_users)
  
  def _get_is_free(self):
    #Checks if class is free
    if self.classcost == 'Free' or self.classcost == 'free':
      return 'Yes'
    else:
      return 'No'
  
  classisfree = property(_get_is_free)
  

  
  
  def __unicode__(self):
    return self.classtitle
  
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    about = models.TextField(blank=True,verbose_name='Something About You',help_text='Who are you?')
    user_photo = models.ImageField(blank=True,verbose_name='Your Photo',upload_to='media/participantphoto/')
    classes_taken = models.ManyToManyField('source',related_name='attended',blank=True)
    classes_taught = models.ManyToManyField('source',related_name='taught',blank=True)
    classes_certified = models.ManyToManyField('source',related_name='certified',blank=True)
    classes_interested = models.ManyToManyField('source',related_name='interested',blank=True)
    hours_given = models.IntegerField(default=0,blank=True)
    website = models.URLField(blank=True,verbose_name='Your Website')
    selfcred_page = models.URLField(blank=True,verbose_name='Your Accreditation',help_text='Do you document your learning online?  Put the URL here!')
    interestedin = models.TextField(blank=True,verbose_name='Interested In Learning',help_text='What are you interested in learning?')
    
    def __str__(self):  
          return "%s's profile" % self.user  
 
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  
 
post_save.connect(create_user_profile, sender=User)
 
User.profile = property(lambda u: u.get_profile() )

