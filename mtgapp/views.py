from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from mtgapp import models, serializers


class CardViewSet(ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    search_fields = ('name',)
