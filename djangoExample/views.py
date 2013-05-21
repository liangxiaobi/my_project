'''
Created on 2013-2-20

@author: lion
'''
from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello World')