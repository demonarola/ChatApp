# -*- coding: utf-8 -*-
from django.urls import re_path, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'register/$', views.register,
            name='register'),
    re_path(r'register_activation_sent/$', views.register_activation_sent,
            name='register_activation_sent'),
    re_path(r'^register_activate/(?P<uidb64>.+)/(?P<token>.+)/$',
            views.register_activate,
            name='activate'),
    # re_path(r'login/$', auth_views.LoginView.as_view(
    #     template_name='accounts/login.html'),
    #     name="login"),
    re_path(r'login/$', views.LoginView.as_view(), name="login"),
    # re_path(r'logout/$', auth_views.LogoutView.as_view(
    #     template_name='accounts/logout.html'),
    #     name="logout"),
    re_path(r'logout/$', views.LogoutView.as_view(), name="logout"),
    # path('non-expiring-token/', views.obtain_persistent_auth_token),
    # path('token/', views.obtain_expiring_auth_token),
]