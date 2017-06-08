# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

#***
# For enabling custom errors
#***
from django.template import RequestContext


# Create your views here.
def home(request):
  return render(request, "main/index.html", {})

# 
# Page not found
# 
def handler404(request):
  response = render_to_response('404.html', {},
                            context_instance=RequestContext(request))
  response.status_code = 404
  return response

# 
# Server Error
# 
def handler500(request):
  response = render_to_response('500.html', {},
                            context_instance=RequestContext(request))
  response.status_code = 500
  return response

# 
# Permission Denied
# 
def handler403(request):
  response = render_to_response('403.html', {},
						context_instance=RequestContext(request))
  response.status_code = 503
  return response

# 
# Page Request
# 
def handler400(request):
  response = render_to_response('400.html', {},
						context_instance=RequestContext(request))

  response.status_code == 400
  return response