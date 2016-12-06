from django import forms 


lista_region = (
	('', '--- seleccionar---'),
	(1, 'Metropolitana'),
	(2, 'Vallez'),
	(3, 'Tropico'),
	(4, 'Cono sur'),
	(5, 'Andina'),
)

class createProyectForm(forms.Form):
	codigo = forms.CharField(max_length=100)
	nombre_proyecto = forms.CharField(max_length=100)
	region = forms.ChoiceField(choices=lista_region)
	municipio = forms.CharField(max_length=100)
	responsable_proyecto = forms.CharField()
	fecha_inicio = forms.CharField()
	fecha_conclucion = forms.CharField()
	objetivo = forms.CharField(max_length=100)
	avance = forms.CharField(max_length=100)

