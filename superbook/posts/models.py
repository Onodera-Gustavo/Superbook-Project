from django.db import models
from heroes.models import Hero


class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."

class Like(models.Model):
    heroi = models.ForeignKey(Hero, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('heroi', 'post')

    def __str__(self):
        return f"{self.heroi.codinome} curtiu {self.post.id}"

