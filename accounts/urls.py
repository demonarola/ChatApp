# -*- coding: utf-8 -*-
from django.urls import re_path
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
    re_path(r'login/$', auth_views.LoginView.as_view(
        template_name='accounts/login.html'),
        name="login"),
    re_path(r'logout/$', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'),
        name="logout"),
    # re_path(r'password_change/$', auth_views.PasswordChangeView.as_view(
    #     template_name='accounts/password_change.html',
    #     success_url='/accounts/password_change_done'),
    #     name="password_change"
    # ),
    # re_path(r'password_change_done/?$', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'),
    #     name="password_change_done"),
    # re_path(r'password_reset/$', auth_views.PasswordResetView.as_view(
    #     template_name='accounts/password_reset.html',
    #     email_template_name='accounts/password_reset_email.html',
    #     subject_template_name='accounts/password_reset_subject.txt',
    #     success_url='/accounts/password_reset_done/',
    #     from_email='support@yoursite.ma'),
    #     # post_reset_redirect='accounts:password_reset_done',
    #     name="password_reset"
    # ),
    # re_path(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         auth_views.PasswordResetConfirmView.as_view(
    #             template_name='accounts/password_reset_confirm.html',
    #             success_url='/accounts/password_reset_complete/'),
    #         name="password_reset_confirm"),
    # re_path(r'password_reset_done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='accounts/password_reset_done.html')),
    # re_path(r'password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='accounts/password_reset_complete.html')),
    #
    # re_path(r'^profile/$', views.view_profile, name='view_profile'),
    # #     re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    # re_path(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    # re_path(r'^change-password/$', views.change_password, name='change_password'),
]