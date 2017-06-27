from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
from django.core.mail import EmailMultiAlternatives


# # -*- coding: utf-8 -*-
# from django.forms import ModelForm
# from car_analytics.models import Movie
# class MovieForm(ModelForm):
#     class Meta:
#         model = Movie
#         fields = ['name','description','anio','category','sort_order']
