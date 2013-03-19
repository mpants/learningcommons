from django.conf.urls import patterns, include, url
from ourschool.views import display_meta_t, display_classes

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^meta/$', display_meta_t),
    url(r'^test-classes/$',display_classes),
    # url(r'^$', 'learningcommons.views.home', name='home'),
    # url(r'^learningcommons/', include('learningcommons.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
