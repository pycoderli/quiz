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
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),



]