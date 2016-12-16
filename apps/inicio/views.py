from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response, get_object_or_404
from django.views.generic import FormView, View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from .forms import LoginForm, UserForm, UserFormedit, reset_form
# PARA ASIGNAR USUARIOS A ROLES
from apps.users.models import User
from apps.inicio.roles import *
from django.template import RequestContext


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


def eliminarUsuario(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return HttpResponseRedirect(reverse_lazy('lista_usuarios'))
# esto es lo que me esta hacindo no lo pongas

# class UserCreate(FormView):
#     form_class = UserForm
#     template_name = 'inicio/user_register.html'
#     success_url = reverse_lazy('lista_usuarios')

#     def form_valid(self, form):
#         user = form.save()
#         roles = form.cleaned_data['roles']
#         userGet = User.objects.get(id=user.id)

#         if roles == 'Admin':
#             Admin.assign_role_to_user(userGet)

#         if roles == 'Supervisor':
#             Operador.assign_role_to_user(userGet)

#         return super(UserCreate, self).form_valid(form)


def UserCreate(request):
    context = RequestContext(request)

    if request.method == 'POST':

        user_form = UserForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            print 'validooooo'
            user = user_form.save()
            # user.empresa = user_form.cleaned_data['empresa']
            user.set_password(user.password)
            user.save()

            rol = user_form.cleaned_data['roles']

            if rol == 'AdminSistema':
                AdminSistema.assign_role_to_user(user)

            if rol == 'Admin':
                Admin.assign_role_to_user(user)

            if rol == 'JefeArea':
                JefeArea.assign_role_to_user(user)

            if rol == 'Supervisor':
                Supervisor.assign_role_to_user(user)

            return HttpResponseRedirect(reverse_lazy('lista_usuarios'))

        else:
            print user_form.errors
    else:
        user_form = UserForm()

    return render_to_response('inicio/user_register.html', {'user_form': user_form}, context)


def logOut(request):
	logout(request)
	return redirect('/')


def ListaUsuarios(request):
    users = User.objects.filter(is_staff=False)
    variables = RequestContext(request, {'usuarios': users})

    return render_to_response('inicio/listado_usuarios.html', variables)


def user_edit(request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserFormedit()

        if request.method == "POST":

            form = UserFormedit(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                # post.author = request.user
                user.save()

                rol = form.cleaned_data['roles']

                if rol == 'admin_sistema':
                    AdminSistema.assign_role_to_user(user)

                if rol == 'admin':
                    Admin.assign_role_to_user(user)

                if rol == 'jefe_area':
                    JefeArea.assign_role_to_user(user)

                if rol == 'supervisor':
                    Supervisor.assign_role_to_user(user)

                return HttpResponseRedirect(reverse_lazy('lista_usuarios'))

        return render(request, 'inicio/update.html', {'user_form': form, 'usere': user})


def change_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = reset_form(request.POST)
        if form.is_valid():
            newpassword = form.cleaned_data['newpassword1']
            user.set_password(newpassword)
            user.save()
            return HttpResponseRedirect(reverse_lazy('lista_usuarios'))

    else:
        form = reset_form()
    content = RequestContext(request, {'form': form, 'user_data': user})
    return render(request, 'inicio/reset_password.html', content,)
