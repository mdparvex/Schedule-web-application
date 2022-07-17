from .models import todo
from django import forms

class todoForms(forms.ModelForm):
	class Meta:
		model = todo
		fields = ['title', 'details','date']

