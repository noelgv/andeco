from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Finanzas(TemplateView):
	template_name = 'finanzas/lista.html'

