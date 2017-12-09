from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class WebdevView(TemplateView):
	template_name='webdev_index.html'

