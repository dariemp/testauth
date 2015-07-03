from django.shortcuts import render_to_response
from models import Distro
from serializer import DistroSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):

    return render_to_response('home.html')

def done(request):

    #login(request)   
  
    list = request.user.social_auth.values_list('provider')
    print list
    l = len(list)
    back_end = list[l-1][0]
    print back_end 
    print request.user.social_auth.filter(provider=request.session['social_auth_last_login_backend'])
    #if backend == 'google-oauth2':
    social_user = request.user.social_auth.filter(provider=back_end,).first()
    #elif backend == 'facebook':
    # social_user = request.user.social_auth.filter(provider='facebook',).first()
    #elif backend == 'linkedin-oauth2':
    #     social_user = request.user.social_auth.filter(provider='linkedin-oauth2',).first()
    # else:
	#return HttpResponse(backend)     
    print social_user
    print social_user.extra_data["access_token"]
    #return HttpResponse(social_user.extra_data["access_token"])
    return render_to_response('done.html',{'user':request.user,'backend':back_end,'token':social_user.extra_data["access_token"]})
 

class DistroList(generics.ListCreateAPIView):
    serializer_class = DistroSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Distro.objects.all()


class DistroDetail(generics.RetrieveDestroyAPIView):
    serializer_class = DistroSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Distro.objects.all()


