from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows':3, 'placeholder':'Escreva seu comentário...'}),
        }
        labels = {
            'autor': 'Herói autor',
            'conteudo': 'Comentário',
        }

    def clean_conteudo(self):
        c = self.cleaned_data.get('conteudo', '').strip()
        if len(c) < 2:
            raise forms.ValidationError('Comentário muito curto.')
        return c
