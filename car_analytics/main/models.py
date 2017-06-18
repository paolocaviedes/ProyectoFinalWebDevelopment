# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Transmision(models.Model):
	tipoTransmision = models.CharField(max_length=10)
	sigla=models.CharField(max_length=2)

class Categoria(models.Model):
	nombreCategoria = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)

class Tipo(models.Model):
	nombreTipo = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
	esParticular=models.BooleanField()
	esAutomotora=models.BooleanField()

class Carroceria(models.Model):
	nombreCarroceria = models.CharField(max_length=100)
	sigla=models.CharField(max_length=10)
