# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from main.tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from main.forms import RegistroForm

# def login(request):
#     context = {}
#     template = loader.get_template('../../django_login/templates/registration/login.html')
#     return HttpResponse(template.render(context, request))

def index(request):
    context = {}
    template = loader.get_template('usersDashboards/Admin/admin_index.html')
    return HttpResponse(template.render(context, request))

def sidebar(request):
    context = {}
    template = loader.get_template('usersDashboards/Admin/admin_sidebar.html')
    return HttpResponse(template.render(context, request))

def new_user(request):
    context = {}
    template = loader.get_template('usersDashboards/Admin/admin_form_nuevousuario.html')
    return HttpResponse(template.render(context, request))

class RegistroUsuario(CreateView):
	model = User
	template_name = "usersDashboards/Admin/admin_form_nuevousuario.html"
	form_class = RegistroForm
	success_url = reverse_lazy('home')
# def movie_form(request):

#     template_name = 'movie/movie_form.html'
#     form = MovieForm(request.POST or None)

#     if form.is_valid() :
#         form.save()
#         return HttpResponseRedirect(reverse('movie_list'))

#     return render(request, template_name, {'form': form})
# Create your views here.

# def nuevo_usuario(request):
# 	if request.method=='POST':
# 		formulario = UserCreationForm(request.POST)
# 		if formulario.is_valid:
# 			formulario.save()
# 			return HttpResponseRedirect('/')
# 	else:
# 		formulario = UserCreationForm()
# 	return render_to_response('nuevousuario.html',{'formulario':formulario},context_instance=RequestContext(request))

