from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login
from social.apps.django_app.utils import psa, load_strategy
from social.apps.django_app.views import _do_login

from .tools import get_access_token


# When we send a third party access token to that view
# as a GET request with access_token parameter,
# python social auth communicate with
# the third party and request the user info to register or

@psa('social:complete')
def register_by_access_token(request, backend):
    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        login(request, user)
        
        return get_access_token(user)
	
    else:
        # If there was an error... you decide what you do here
        return HttpResponse("error")
