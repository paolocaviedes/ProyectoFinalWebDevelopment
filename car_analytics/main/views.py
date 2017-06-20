# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))
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