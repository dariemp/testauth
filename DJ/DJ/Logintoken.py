'''
Created on Jul 3, 2015

@author: jrabelo
'''

from django.shortcuts import render_to_response
from DJ.settings import PROVIDER

def accessToken(strategy,backend,user,response, *args, **kwargs):
    
    PROVIDER = str(backend).split(".")
    print PROVIDER   

    return None
