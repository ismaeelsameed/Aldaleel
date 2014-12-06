from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def home(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def companies(request, template_name='page-portfolio-3-columns-1.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))