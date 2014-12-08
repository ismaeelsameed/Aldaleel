from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def home(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def companies(request, template_name='companies.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def about(request, template_name='about.html'):
    return render_to_response(template_name,context_instance=RequestContext(request))