import pytz
from datetime import datetime

from rest_framework.exceptions import AuthenticationFailed
import rest_framework.authentication

from .models import Token
from ChatProject import settings


class TokenAuthentication(rest_framework.authentication.TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - settings.TOKEN_EXPIRE_TIME:
            token.delete()
            raise AuthenticationFailed('Token has expired')

        return token.user, token
