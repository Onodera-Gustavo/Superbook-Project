
from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia']

