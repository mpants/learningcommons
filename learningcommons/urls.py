from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^meta/$', 'ourschool.views.display_meta_t', name='meta'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ourschool.views.home', name='home'),
    url(r'^test/', 'ourschool.views.test', name='test'),
    url(r'^viewlearning/', 'ourschool.views.viewlearning',name='viewlearning'),
    url(r'^view-all/$','ourschool.views.viewall',name='viewall'),
    #url(r'^search/$','ourschool.views.search',name='search'),
    url(r'^submitlearning/$','ourschool.views.submitlearning',name='submitlearning'),
    # url(r'^learningcommons/', include('learningcommons.foo.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
