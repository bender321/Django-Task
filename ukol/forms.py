from django import forms
from . import models


class CreateEntrepreneur(forms.ModelForm):
	class Meta:
		model = models.Entrepreneur
		fields = ['name', 'mail', 'ico']