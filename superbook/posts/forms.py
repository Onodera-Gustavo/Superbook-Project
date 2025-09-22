from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva sua mensagem...'}),
        }
        labels = {
            'autor': 'Herói autor',
            'mensagem': 'Mensagem',
        }

    def clean_mensagem(self):
        msg = self.cleaned_data.get('mensagem', '').strip()
        if len(msg) < 3:
            raise forms.ValidationError('A mensagem deve ter pelo menos 3 caracteres.')
        return msg