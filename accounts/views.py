# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext as _
from django.utils.translation import activate

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from django.template.loader import render_to_string
from .models import Token
from django.contrib.auth.signals import user_logged_in
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

from accounts.models import User

from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from .tokens import account_activation_token


User = get_user_model()

activate('es')


@api_view(['GET', 'POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    """
    View register (sign up).
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = _('Enable your account')
            message = render_to_string('email/account_activation_email.html', {
                'user': user, 
                'rest_api': False,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:register_activation_sent')
        else:
            messages.warning(request, form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html',
                  {'form': form})


def register_activation_sent(request):
    """
    View after register.
    """
    return render(request, 'accounts/register_activation_sent.html')


def register_activate(request, uidb64, token):
    """
    Activate user after register.
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        messages.info(request, _("Your account has been enabled."))
        return redirect('home')
    else:
        return render(request, 'accounts/register_activation_invalid.html')

class LoginView(APIView):

    def post(self, request, format=None):
        print(request.data,"---------")
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        django_login(request, user)

        # token_ttl = self.get_token_ttl()
        print(request.user)
        token = Token.objects.create(user=request.user)
        user_logged_in.send(sender=user.__class__,
                            request=request, user=user)
        data = {
            'user': user.username,
            'token': token.key
        }
        return Response(data)


class LogoutView(APIView):
    # authentication_classes = (TokenAuthentication, )

    def post(self, request):
        request.auth.delete()
        logout(request)
        return Response("Logout Successful!", status=204)
