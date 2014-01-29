from django.db.models import Q

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from mtgapp import models, serializers


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user and not obj.private


def non_empty_split(s):
    return filter(lambda f: len(f) > 0, s.split(','))


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
    permission_classes = (IsOwnerOrReadOnly,)
    paginate_by = 15
    paginate_by_param = 'page'
    max_paginate_by = 150
    search_fields = ('title',)

    @action(methods=['POST'])
    def add_cards(self, request, *args, **kwargs):
        pass

    @action(methods=['POST'])
    def remove_cards(self, request, *args, **kwargs):
        pass

    def get_queryset(self):
        if self.request.user.is_authenticated():
            queryset = models.Deck.objects.filter(user=self.request.user)
            return queryset.order_by('title')
        return []
