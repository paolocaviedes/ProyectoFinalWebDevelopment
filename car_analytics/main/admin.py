# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Transmision

class TransmisionAdmin(admin.ModelAdmin):
	list_display = ('id','tipoTransmision','sigla')

admin.site.register(Transmision,TransmisionAdmin)

# Register your models here.
