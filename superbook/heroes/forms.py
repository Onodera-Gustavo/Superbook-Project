
from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ["codinome", "nome_real", "email_contato", "poder_principal", "cidade", "historia"]
        widgets = {"historia": forms.Textarea(attrs={"rows":4})}

