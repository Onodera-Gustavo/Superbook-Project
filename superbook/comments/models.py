from django.db import models
from posts.models import Post
from heroes.models import Hero

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Hero, on_delete=models.SET_NULL, null=True, blank=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        autor = self.autor.codinome if self.autor else "Anon"
        return f"Comentário de {autor} em {self.post.pk}"
