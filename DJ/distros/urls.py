'''
Created on Jun 25, 2015

@author: jrabelo
'''

from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import  views

urlpatterns = patterns(
    '',
    url(r'^$', views.DistroList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.DistroDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)
