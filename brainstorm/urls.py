from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login
from django.urls import path
from django.contrib.auth import views as auth_views
from .models import level


urlpatterns =  [
    path('',views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('levels/level<int:levelnum>/',views.levels),
    path('login/', auth_views.login, {'template_name': 'login.html','extra_context': {'next':'levels/level<int:levelnum>/'}}, name='login'),
   
    path('signup/', views.signup, name='signup'),
    path('results/',views.results,name='results'),



]