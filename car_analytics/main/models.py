# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Transmision(models.Model):
	tipoTransmision = models.CharField(max_length=10)
	sigla=models.CharField(max_length=2)


