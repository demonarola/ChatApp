# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext as _
from django.utils.translation import activate

from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from django.template.loader import render_to_string
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


# @login_required
# @api_view(['GET'])
# def view_profile(request, pk=None):
#     if pk:
#         user = User.objects.get(pk=pk)
#     else:
#         user = request.user
#     args = {'user': user}
#     return render(request, 'accounts/profile.html', args)
#
#
# @login_required
# @api_view(['GET', 'POST', 'PUT'])
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             messages.info(request, _("Your information has been updated!"))
#         else:
#             messages.warning(request, form.errors)
#         return redirect(reverse('accounts:view_profile'))
#     else:
#         form = EditProfileForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/profile_edit.html', args)
#
#
# @login_required
# @api_view(['GET', 'POST', 'PUT'])
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.info(request, _("Your Password has been updated!"))
#             return redirect(reverse('accounts:view_profile'))
#         else:
#             messages.warning(request, form.errors)
#             return redirect(reverse('accounts:change_password'))
#     else:
#         form = PasswordChangeForm(user=request.user)
#
#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)
#
#     msg = EmailMultiAlternatives(
#         # title:
#         _("Password Reset for {title}").format(title="Tranki App"),
#         # message:
#         email_plaintext_message,
#         # from:
#         settings.DEFAULT_FROM_EMAIL,
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()
