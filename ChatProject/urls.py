"""ChatProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.i18n import JavaScriptCatalog
from django.views.generic import RedirectView, TemplateView
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'^chat/', include(('chat.urls', 'chat'), namespace='chat')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    # re_path(r'^(?:.*)/?$', TemplateView.as_view(
    #     template_name='accounts/profile.html'), name='home'),
    # re_path(r'api/auth/', include('knox.urls')),
    # re_path(r'api/auth/login_user/', LoginView.as_view()),
    path('api/v1/', include((router.urls, 'chats'), namespace='api'))
]
