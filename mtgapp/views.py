from django.db.models import Q

from rest_framework.viewsets import ModelViewSet

from mtgapp import models, serializers


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
        return queryset.order_by('name')
