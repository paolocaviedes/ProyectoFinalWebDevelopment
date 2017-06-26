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


from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from main.forms import SignUpForm
from main.tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

