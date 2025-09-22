from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['post', 'autor', 'criado_em']
    search_fields = ['post__mensagem', 'autor__codinome', 'conteudo']
    list_filter = ['criado_em']
