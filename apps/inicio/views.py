from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import FormView, View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from .forms import LoginForm



class Index(View):
	def get(self, request, *args, **kwargs):

		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse_lazy('login'))
		else:
			return HttpResponseRedirect(reverse_lazy('inicio'))


class Inicio(TemplateView):
	template_name = 'inicio/index.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Inicio, self).dispatch(*args, **kwargs)


  	  
class loginview(FormView):

    form_class = LoginForm
    template_name = 'inicio/login.html'
    success_url = reverse_lazy("inicio")

    def form_valid(self, form): 
    	login(self.request, form.get_user())
        return super(loginview, self).form_valid(form)


def logOut(request):
	logout(request)
	return redirect('/')
        	