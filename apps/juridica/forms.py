from django import forms 


class ConveniosForm(forms.Form):
	fecha = forms.DateField(label='fecha')
	entidad = forms.CharField(max_length=100)
	objetivo = forms.CharField(max_length=100)
	contra_financiera = forms.CharField(label='contraparte financiera', max_length=100)
	vig_avance = forms.CharField(label='vigencia/avance', max_length=100)
