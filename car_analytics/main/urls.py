from django.conf.urls import url,include
from main import views
# from django_login import views as djlogin

urlpatterns = [
                # Matches any html file - to be used for gentella   
                # Avoid using your .html in your resources. Or create a separate django app.
                # url(r'^.*\.html', views.gentella_html, name='gentella'),    

                # The home page  
                url(r'^$', views.index, name='index'),
				url(r'^sidebar', views.sidebar, name='sidebar'),
				url(r'^crear_usuario', views.new_user, name='nuevo_usuario'),
              ]