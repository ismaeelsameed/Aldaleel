from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
from aldaleel.models import Company


def home(request, template_name='index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))


def companies(request, template_name='companies.html'):
    all_companies = Company.objects.all()
    return render_to_response(template_name, {"companies": all_companies}, context_instance=RequestContext(request))


def about(request, template_name='about.html'):
    return render_to_response(template_name,context_instance=RequestContext(request))


def company_details(request, company_id, template_name='company-details.html'):
    company = Company.objects.get(id=company_id)
    return render_to_response(template_name, {"company": company}, context_instance=RequestContext(request))