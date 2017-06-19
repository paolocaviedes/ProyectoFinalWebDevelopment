# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Transmision,Categoria,Carroceria,Pais,Region,Ciudad,Marca,Modelo,Version,Tipo,Particular,Automotora,Contacto,Vehiculo,ContactoVehiculo,TipoCambio,Edicion

class TransmisionAdmin(admin.ModelAdmin):
	list_display = ('id','tipoTransmision','sigla')

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombreCategoria','sigla')

class CarroceriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombreCarroceria','sigla')

class PaisAdmin(admin.ModelAdmin):
	list_display = ('id','nombrePais','sigla')

class RegionAdmin(admin.ModelAdmin):
	list_display = ('id','nombreRegion','numero','sigla','pais')

class CiudadAdmin(admin.ModelAdmin):
	list_display = ('id','nombreCiudad','sigla','region')

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('id','nombreMarca','paisDeOrigen','sigla')

class ModeloAdmin(admin.ModelAdmin):
	list_display = ('id','nombreModelo','sigla','marca')

class VersionAdmin(admin.ModelAdmin):
	list_display = ('id','nombreVersion','sigla','descripcion','modelo')

class TipoAdmin(admin.ModelAdmin):
	list_display = ('id','nombreTipo','sigla','esAutomotora','esParticular')

class ParticularAdmin(admin.ModelAdmin):
	list_display = ('id','nombreParticular','personalIdentifier','direccion','telefono','email','tipo','ciudad')

class AutomotoraAdmin(admin.ModelAdmin):
	list_display = ('id','nombreAutomotora','direccion','comuna','telefono','email','tipo','ciudad')

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('id','nombreContacto','direccion','comuna','telefono','email','tipo','ciudad','automotora')

class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('id','kilometraje','precio','anno','puertas','cilindrada','colorExterior','combustible','direccion','esNuevo','aireAcondicionado','alzavidriosElectricos','espejosElectricos','frenosAbs','airbag','unicoDuenno','cierreCentralizado','convertidorCatalitico','llantas','radio','vendido','fechadePublicacion','version','modelo','marca','tipo','ciudad','carroceria','categoria','transmision')	

class ContactoVehiculoAdmin(admin.ModelAdmin):
	list_display = ('id','vehiculo','contacto')

class TipoCambioAdmin(admin.ModelAdmin):
	list_display = ('id','nombreTipoCambio','sigla')

class EdicionAdmin(admin.ModelAdmin):
	list_display = ('id','fechadePublicacion','valorAnterior','valorNuevo','campoEditado','vehiculo','tipoCambio')

admin.site.register(Transmision,TransmisionAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Carroceria,CarroceriaAdmin)
admin.site.register(Pais,PaisAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Modelo,ModeloAdmin)
admin.site.register(Version,VersionAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Particular,ParticularAdmin)
admin.site.register(Automotora,AutomotoraAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(ContactoVehiculo,ContactoVehiculoAdmin)
admin.site.register(TipoCambio,TipoCambioAdmin)
admin.site.register(Edicion,EdicionAdmin)

# Register your models here.
