from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser


class TokenAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        headers = dict(scope['headers'])
        if scope.get('query_string'):
            query_string = scope['query_string']
            all_params = query_string.decode().split('&')
            for param in all_params:
                if 'token' in param.lower():
                    token_name, token_key = param.split('=')
                    try:
                        if token_name.lower() == 'token':
                            token = Token.objects.get(key=token_key)
                            scope['user'] = token.user
                    except Exception as e:
                        print('Error: TokenAuthMiddleware: ', e)
                    break
        elif b'authorization' in headers:
            try:
                token_name, token_key = headers[b'authorization'].decode().split()
                if token_name == 'Token':
                    token = Token.objects.get(key=token_key)
                    scope['user'] = token.user
            except Token.DoesNotExist:
                scope['user'] = AnonymousUser()
        return self.inner(scope)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))
