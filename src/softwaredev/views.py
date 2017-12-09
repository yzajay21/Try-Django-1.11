from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class SoftwareView(TemplateView):
	template_name ='software.html'
