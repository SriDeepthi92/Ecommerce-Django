from django.urls import path, include
from home import views
from django.contrib.auth.views import LoginView


urlpatterns = [
   #path('', views.index, name='home'), 
   path('', views.home, name='home'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
]