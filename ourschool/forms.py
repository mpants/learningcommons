from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from models import source
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)
   
  class Meta:
    model = User
    fields = ("username","email" )

class sourceform(ModelForm):
  class Meta:
    model = source
    exclude = ('classusers','classinterested','classcertified','classteachers','classurl',)

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
  
class addlearning(forms.Form):
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
  #make class label suggestions randomly generated
  title = forms.CharField(max_length=100,label='A short title for your learning, i.e. "Biodynamic Telescope Deconstruction"')
  subject = forms.CharField(max_length=50,label='The subject of your learning, i.e. "Cognitive Science"')
  format = forms.ChoiceField(choices=FORMAT_CHOICES)
  host = forms.CharField(max_length=70,label='The person or organization coordinating or hosting your learning')
  date = forms.DateField(required=False,label='Most likely starting date for the first (or only) learning session')
  
  '''
  def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
  '''