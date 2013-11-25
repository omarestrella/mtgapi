from rest_framework import serializers, pagination

from mtgapp import models


class CardSerializer(serializers.ModelSerializer):
    types = serializers.RelatedField(many=True)
    set = serializers.RelatedField()
    colors = serializers.RelatedField(many=True)
    subtypes = serializers.RelatedField(many=True)

    class Meta:
        model = models.Card
