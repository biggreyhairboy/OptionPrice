from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
#from OptionPricePanel.views import hello, homepage,systime,optionpricemain
from OptionPricePanel.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OptionPrice.views.home', name='home'),
    #url(r'^OptionPrice/', include('OptionPrice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', systime),
    ('^Price/$', optionpricemain),

    ('^OptionPriceCalculator/$', optionpricecalculator),
    ('^OptionPriceCalculator/[^/]+', calc),
    ('^$', homepage),

)
