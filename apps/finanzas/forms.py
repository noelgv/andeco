# -*- coding: utf-8 -*-
from django import forms
from .models import Cursos


lista_region = (
    ('', '--- seleccionar---'),
    (1, 'Metropolitana'),
    (2, 'Vallez'),
    (3, 'Tropico'),
    (4, 'Cono sur'),
    (5, 'Andina'),
)

lista_estado = (
	('No iniciado', 'No iniciado'),
    ('En proceso', 'En proceso'),
    ('Finalizado', 'Finalizado'),
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


class AsistenciaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    region = forms.ChoiceField(choices=lista_region)
    municipio = forms.CharField(max_length=100)
    responsable = forms.CharField()
    fecha_inicio = forms.CharField()
    fecha_conclucion = forms.CharField()
    objetivo = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':3}))
    estado = forms.ChoiceField(choices=lista_estado)


list_of_choices = (
    ("cochabamba", "cochabamba"),
    ("Colcapirhua", "Colcapirhua"),
    ("Quillacollo", "Quillacollo"),
    ("Sacaba", "Sacaba"),
    ("Sipe Sipe", "Sipe Sipe"),
    ("Vinto", "Vinto"),
    ("Punata", "Punata"),
    ("Capinota", "Capinota"),
    ("Santivañes", "Santivañes"),
    ("Arani", "Arani"),
    ("Villa Rivero", "Villa Rivero"),
    ("Cliza", "Cliza"),
    ("Toco", "Toco"),
    ("Tolata", "Tolata"),
    ("Tarata", "Tarata"),
    ("Anzaldo", "Anzaldo"),
    ("Sacabamba", "Sacabamba"),
    ("Arbieto", "Arbieto"),
    ("Tacahi", "Tacahi"),
    ("Villa Gualberto Villarroel", "Villa Gualberto Villarroel"),
    ("San Benito", "San Benito"),
    ("Entre Rios", "Entre Rios"),
    ("Shinahota", "Shinahota"),
    ("Colomi", "Colomi"),
    ("Puerto Villarroel", "Puerto Villarroel"),
    ("Villa Tunari", "Villa Tunari"),
    ("Chimore", "Chimore"),
    ("Vacas", "Vacas"),
    ("Tiraque", "Tiraque"),
    ("Alalay", "Alalay"),
    ("Mizque", "Mizque"),
    ("Aiquile", "Aiquile"),
    ("Vila Vila", "Vila Vila"),
    ("Pojo", "Pojo"),
    ("Omereque", "Omereque"),
    ("Totora", "Totora"),
    ("Pocona", "Pocona"),
    ("Pasorapa", "Pasorapa"),
    ("Bolivar", "Bolivar"),
    ("Cocapata", "Cocapata"),
    ("independencia", "independencia"),
    ("Morochata", "Morochata"),
    ("Tapacari", "Tapacari"),
    ("Tacopaya", "Tacopaya"),
    ("Sicaya", "Sicaya"),
    ("Arque", "Arque"),
)


class CursoForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    area = forms.CharField()
    costo = forms.DecimalField()
    material = forms.CharField(max_length=100)
    region = forms.ChoiceField(choices=lista_region)
    # choice_field = forms.MultipleChoiceField(choices=list_of_choices)
    municipios = forms.MultipleChoiceField(choices=list_of_choices)
    responsable = forms.CharField()
    fecha_inicio = forms.CharField()
    fecha_conclucion = forms.CharField()
    objetivo = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':3}))


class CursoEditForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100)
    area = forms.CharField()
    costo = forms.DecimalField()
    material = forms.CharField(max_length=100)
    region = forms.ChoiceField(choices=lista_region)
    # choice_field = forms.MultipleChoiceField(choices=list_of_choices)
    municipios = forms.MultipleChoiceField(choices=list_of_choices)
    responsable = forms.CharField()
    fecha_inicio = forms.CharField()
    fecha_conclucion = forms.CharField()
    objetivo = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model = Cursos
        fields = ('titulo', 'area', 'costo', 'material', 'region', 'municipios', 'responsable', 'fecha_inicio', 'fecha_conclucion', 'objetivo')
