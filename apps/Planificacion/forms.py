from django import forms 


class responsablesForm(forms.Form):
	nombre = forms.CharField(label='nombre')
	codigo = forms.CharField(max_length=100)
	ci = forms.CharField(max_length=100)
	telefono = forms.CharField(label='telefono', max_length=100)
	direccion = forms.CharField(label='direccion', max_length=100)


# class proyectosForm(forms.Form):
# 	cod = forms.CharField(max_length=100)
# 	nombre = forms.CharField(label='nombre')
# 	porcentaje_global = forms.CharField(label='porcentaje_global')


lista_region = (
	('', '--- seleccionar---'),
	(1, 'Metropolitana'),
	(2, 'Vallez'),
	(3, 'Tropico'),
	(4, 'Cono sur'),
	(5, 'Andina'),
)


class proyectosForm(forms.Form):
	regiones = forms.ChoiceField(choices=lista_region)
	municipios = forms.CharField(max_length=100)
	nombre_proyecto = forms.CharField()
	responsable_proyecto = forms.CharField()
	responsable_seguimiento = forms.CharField()
	