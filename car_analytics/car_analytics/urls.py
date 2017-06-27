"""car_analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from main import views as main_views
from main.views import RegistroUsuario
urlpatterns = [
    # login
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),

    #user_management
    url(r'^crear_usuario$', RegistroUsuario.as_view(), name='nuevousuario'),
    url(r'^home/crear_usuario$', RegistroUsuario.as_view(), name='nuevousuario'),

    url(r'^listar_usuarios$', main_views.user_list, name='movie_list'),
    url(r'^home/listar_usuarios$', main_views.user_list, name='movie_list'),

    url(r'^edit/(?P<pk>\d+)$', main_views.user_update, name='user_edit'),
    url(r'^delete/(?P<pk>\d+)$', main_views.user_delete, name='user_delete'),


    # admin
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', admin.sqite.urls),
    # url(r'^main/templates/nuevo$','principal.views.nuevo_usuario'),
    url(r'^main/', include('main.urls')),
    url(r'^', include('main.urls')),
]
