from django.contrib import admin
from . import models
# from django.utils.translation import gettext_lazy as _

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)

