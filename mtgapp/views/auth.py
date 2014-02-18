import json

from django import http
from django.views import generic
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class AuthenticationView(generic.View):
    def user_response(self, user):
        return {
            'user': dict(id=user.id, username=user.username),
            'token': user.auth_token.key
        }

    def authenticate_with_credentials(self, username, password):
        user = authenticate(username=username, password=password)
        if not user:
            return False
        return user

    def authenticate_with_token(self, token):
        user = authenticate(token=token)
        if not user:
            return False
        return user

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticationView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = self.authenticate_with_credentials(username, password)
        elif token:
            user = self.authenticate_with_token(token)
        else:
            return http.HttpResponse('Token required', status=500)
        if not user:
            return http.HttpResponse('Username and/or password incorrect', status=500)
        login(request, user)
        response = self.user_response(user)
        return http.HttpResponse(json.dumps(response), content_type='application/json')


class LogoutView(generic.View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return http.HttpResponse('')


class RegistrationView(generic.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pass
