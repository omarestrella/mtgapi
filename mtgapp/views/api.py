import json
import logging

from django import http
from django.views import generic
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

import redis

from mtgapp import models, serializers


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user and not obj.private


def non_empty_split(s):
    return filter(lambda f: len(f) > 0, s.split(','))


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


class RegistrationView(generic.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pass


class CardViewSet(ModelViewSet):
    model = models.Card
    paginate_by = 75
    paginate_by_param = 'page'
    max_paginate_by = 150
    search_fields = ('name', 'text',)

    def name_filter(self, queryset, filter_field):
        filter_args = self.request.QUERY_PARAMS.get(filter_field, '')
        filter_args = non_empty_split(filter_args)
        if filter_args and len(filter_args) > 0:
            query = Q()
            for arg in filter_args:
                key = '{}__name__iexact'.format(filter_field)
                param = {key: arg}
                query |= Q(**param)
            return queryset.filter(query)
        return queryset

    def set_filter(self, queryset):
        set = self.request.QUERY_PARAMS.get('set', '')
        if set and len(set) == 3:
            return queryset.filter(card_set__code__iexact=set)
        return queryset

    def cmc_filter(self, queryset):
        cmc = self.request.QUERY_PARAMS.get('cmc', '');
        if cmc:
            return queryset.filter(cmc=cmc)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.LimitedCardSerializer
        else:
            return serializers.CardSerializer

    def get_queryset(self):
        queryset = models.Card.objects.all()
        queryset = self.name_filter(queryset, 'colors')
        queryset = self.name_filter(queryset, 'types')
        queryset = self.set_filter(queryset)
        queryset = self.cmc_filter(queryset)
        return queryset.order_by('name')


class DeckViewSet(ModelViewSet):
    model = models.Deck
    serializer_class = serializers.DeckSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    paginate_by = 15
    paginate_by_param = 'page'
    max_paginate_by = 150
    search_fields = ('title',)

    @action(methods=['POST'])
    def update_cards(self, request, *args, **kwargs):
        """
        [{
            "card": <number>
            "count": <number|optional>
        }]
        """
        json_cards = json.loads(request.DATA.get('data'))
        deck_id = kwargs.get('pk')
        deck = models.Deck.objects.get(id=deck_id)
        for card_data in json_cards:
            card_id = card_data.get('card')
            count = card_data.get('count')
            if models.DeckCard.objects.filter(card__id=card_id).exists():
                deck_card = models.DeckCard.objects.get(card__id=card_id)
                if count == 0:
                    deck_card.delete()
                else:
                    if not count:
                        deck_card.count += 1
                    else:
                        deck_card.count = count
                    deck_card.save()

            else:
                card = models.Card.objects.get(id=card_id)
                models.DeckCard.objects.create(card=card, count=1, deck=deck)
        return http.HttpResponse(json.dumps({}), mimetype='application/json')

    def get_queryset(self):
        if self.request.user.is_authenticated():
            queryset = models.Deck.objects.filter(user=self.request.user)
            return queryset.order_by('title')
        return []
