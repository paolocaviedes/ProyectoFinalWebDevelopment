# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Transmision,Categoria

class TransmisionAdmin(admin.ModelAdmin):
	list_display = ('id','tipoTransmision','sigla')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombreCategoria','sigla')

admin.site.register(Transmision,TransmisionAdmin)
admin.site.register(Categoria,CategoriaAdmin)

# Register your models here.
