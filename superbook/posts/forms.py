from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor', 'mensagem']  # autor é um Hero
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escreva sua mensagem...'
            })
        }
        labels = {
            'autor': 'Herói autor',
            'mensagem': 'Mensagem'
        }

    def clean_mensagem(self):
        msg = self.cleaned_data.get('mensagem', '').strip()
        if len(msg) < 5:
            raise forms.ValidationError("A mensagem deve ter ao menos 5 caracteres.")
        return msg
