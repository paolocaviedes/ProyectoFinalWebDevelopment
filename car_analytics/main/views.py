# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required


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