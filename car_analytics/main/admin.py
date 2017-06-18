# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Transmision,Categoria,Tipo

class TransmisionAdmin(admin.ModelAdmin):
	list_display = ('id','tipoTransmision','sigla')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombreCategoria','sigla')

class TipoAdmin(admin.ModelAdmin):
	list_display = ('id','nombreTipo','sigla','esAutomotora','esParticular')

admin.site.register(Transmision,TransmisionAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tipo,TipoAdmin)

# Register your models here.
