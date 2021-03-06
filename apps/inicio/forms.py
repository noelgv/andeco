# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from apps.users.models import User


class LoginForm(AuthenticationForm):
    pass


# class Userform(UserCreationForm):
#     CHOICES = (
#         ('', 'selecciona'),
#         ('Admin', 'Administrador'),
#         ('Supervisor', 'Supervisor'),
     
#     )
#     roles = forms.ChoiceField(choices=CHOICES, required=True, label='Rol')

list_of_choices = (
    ('', 'selecciona'),
    ('AdminSistema', 'Administrador Sistema'),
    ('Admin', 'Administrador'),
    ('JefeArea', 'Jefe Area'),
    ('Supervisor', 'Supervisor'),
)

list_of_edit = (
    ('', 'selecciona'),
    ('admin_sistema', 'Administrador Sistema'),
    ('admin', 'Administrador'),
    ('jefe_area', 'Jefe Area'),
    ('supervisor', 'Supervisor'),
)

list_of_area = (
    ('', 'selecciona'),
    ('Planificacion', 'Planificacion'),
    ('Finanzas', 'Finanzas'),
    ('Juridica', 'Juridica'),
)


class UserForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre")
    p_apellido = forms.CharField(label="Primer apellido")
    s_apellido = forms.CharField(required=False, label="Segundo apellido")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=30, render_value=False)), label="Contraseña (confirmación):")
    roles = forms.ChoiceField(choices=list_of_choices)
    area = forms.ChoiceField(required=False, choices=list_of_area)

    class Meta:
        model = User
        fields = ('nombre', 'p_apellido', 'area', 's_apellido', 'username', 'password')

    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist:
            return self.cleaned_data['username']

        raise forms.ValidationError("este usuario ya existe")

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Los dos campos de contraseña no coinciden.")
        return self.cleaned_data


class UserFormedit(forms.ModelForm):
    nombre = forms.CharField(label="Nombre")
    p_apellido = forms.CharField(label="Primer apellido")
    s_apellido = forms.CharField(required=False, label="Segundo apellido")
    roles = forms.ChoiceField(choices=list_of_edit)
    area = forms.ChoiceField(required=False, choices=list_of_area)

    class Meta:
        model = User
        fields = ('nombre', 'p_apellido', 's_apellido', 'username')


class reset_form(forms.Form):
    newpassword1 = forms.CharField(max_length=20, label="Contraseña", widget=forms.TextInput(attrs={'type':'password',  'class' : 'span'}))
    newpassword2 = forms.CharField(max_length=20, label="Contraseña (de nuevo)", widget=forms.TextInput(attrs={'type':'password',  'class' : 'span'}))

    def clean(self):
        if 'newpassword1' in self.cleaned_data and 'newpassword2' in self.cleaned_data:
            if self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
                raise forms.ValidationError("Los dos campos de contraseña no coinciden.")
        return self.cleaned_data
