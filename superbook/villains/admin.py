from django.contrib import admin
from .models import Villain

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_real', 'poder_principal', 'cidade', 'email_contato', 'criado_em']
    list_filter = ['cidade']
    search_fields = ['nome', 'nome_real', 'cidade', 'email_contato']
    readonly_fields = ['criado_em']
    fieldsets = (
        ('Identidade', {
            'fields': ('nome', 'nome_real', 'email_contato')
        }),
        ('Informações', {
            'fields': ('poder_principal', 'cidade', 'historia')
        }),
        ('Dados', {
            'fields': ('criado_em',)
        }),
    )
