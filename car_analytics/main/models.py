# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Transmision(models.Model):
	tipoTransmision = models.CharField(max_length=10)
	sigla=models.CharField(max_length=2)

class Categoria(models.Model):
	nombreCategoria = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)

class Carroceria(models.Model):
	nombreCarroceria = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)

class Pais(models.Model):
	nombrePais = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)

class Region(models.Model):
	nombreRegion = models.CharField(max_length=100)
	numero = models.IntegerField()
	sigla=models.CharField(max_length=10)
	pais = models.ForeignKey(Pais)

class Ciudad(models.Model):
	nombreCiudad = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
	region = models.ForeignKey(Region)

class Marca(models.Model):
	nombreMarca = models.CharField(max_length=100)
	paisDeOrigen = models.ForeignKey(Pais)
	sigla=models.CharField(max_length=10)

class Modelo(models.Model):
	nombreModelo = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
	marca = models.ForeignKey(Marca)

class Version(models.Model):
	nombreVersion = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
	descripcion = models.CharField(max_length=250)
	modelo = models.ForeignKey(Modelo)

class Tipo(models.Model):
	nombreTipo = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
	esParticular=models.BooleanField()
	esAutomotora=models.BooleanField()

class Particular(models.Model):
	nombreParticular = models.CharField(max_length=100)
	personalIdentifier = models.IntegerField()
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField()
	email = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	ciudad = models.ForeignKey(Ciudad)

class Automotora(models.Model):
	nombreAutomotora = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	comuna = models.CharField(max_length=200)
	telefono = models.IntegerField()
	email = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	ciudad = models.ForeignKey(Ciudad)

class Contacto(models.Model):
	nombreContacto = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	comuna = models.CharField(max_length=200)
	telefono = models.IntegerField()
	email = models.CharField(max_length=100)
	tipo = models.ForeignKey(Tipo)
	ciudad = models.ForeignKey(Ciudad)
	automotora = models.ForeignKey(Automotora)

class Vehiculo(models.Model):
	kilometraje = models.IntegerField()
	precio = models.IntegerField()
	anno = models.IntegerField()
	puertas = models.IntegerField()
	cilindrada = models.IntegerField()
	colorExterior = models.CharField(max_length=100)
	combustible = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	esNuevo = models.BooleanField()
	aireAcondicionado = models.BooleanField()
	alzavidriosElectricos = models.BooleanField()
	espejosElectricos = models.BooleanField()
	frenosAbs = models.BooleanField()
	airbag = models.BooleanField()
	unicoDuenno = models.BooleanField()
	cierreCentralizado = models.BooleanField()
	convertidorCatalitico = models.BooleanField()
	llantas = models.BooleanField()
	radio = models.BooleanField()
	vendido = models.BooleanField()
	fechadePublicacion = models.DateTimeField(auto_now=True, auto_now_add=False)
	version = models.ForeignKey(Version)
	modelo = models.ForeignKey(Modelo)
	marca = models.ForeignKey(Marca)
	tipo = models.ForeignKey(Tipo)
	ciudad = models.ForeignKey(Ciudad)
	carroceria = models.ForeignKey(Carroceria)
	categoria = models.ForeignKey(Categoria)
	transmision = models.ForeignKey(Transmision)

class ContactoVehiculo(models.Model):
	vehiculo = models.ForeignKey(Vehiculo)
	contacto = models.ForeignKey(Contacto)

class TipoCambio(models.Model):
	nombreTipoCambio = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)

class Edicion(models.Model):
	fechadePublicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
	valorAnterior = models.CharField(max_length=200)
	valorNuevo = models.CharField(max_length=200)
	campoEditado = models.CharField(max_length=200)
	vehiculo = models.ForeignKey(Vehiculo)
	tipoCambio = models.ForeignKey(TipoCambio)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
