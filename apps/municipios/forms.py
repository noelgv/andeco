from django import forms 


class municipiosForm(forms.Form):
    cod_municipio = forms.CharField(label='cod_municipio')
    nombre = forms.CharField(max_length=100)


class provinciasForm(forms.Form):
    cod_provincia = forms.CharField(label='cod_provincia')
    nombre = forms.CharField(max_length=100)
