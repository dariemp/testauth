'''
Created on Jun 30, 2015

@author: jrabelo
'''

from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token),
)
