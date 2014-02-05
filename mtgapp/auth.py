from django.contrib.auth.models import User


class TokenModelBackend(object):
    def authenticate(self, token=None):
        try:
            return User.objects.get(auth_token__key=token)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
