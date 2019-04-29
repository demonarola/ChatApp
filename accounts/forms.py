# -*- coding: utf-8 -*-
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _

from .widgets import BootstrapDateTimePickerInput

User = get_user_model()


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text=_('Insert your name'), widget=forms.TextInput(attrs={
        'placeholder': _('Name'),
        'autocomplete': 'off',
    }))
    last_name = forms.CharField(max_length=30, required=True, help_text=_('Insert your last name'), widget=forms.TextInput(attrs={
        'placeholder': _('Last Name'),
    }))
    email = forms.EmailField(
        required=True,
        max_length=254,
        help_text=_('Insert a valid email.'),
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
        }
        ))
    birth_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=BootstrapDateTimePickerInput(),
        help_text=_('Format: YYYY-MM-DD'),
    )

    def clean_birth_date(self):
        dob = self.cleaned_data['birth_date']

        age = (datetime.date.today() - dob).days/365
        if age < 18 or age > 150:
            raise ValidationError(_('Insert a valid Birthdate.'))

        return dob

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'password1',
            'password2',
            'telephone',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name = '/something/else'
    password = None

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'telephone',
        )
