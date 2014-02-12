from rest_framework import serializers, pagination

from mtgapp import models


class CardSerializer(serializers.ModelSerializer):
    types = serializers.RelatedField(many=True)
    card_set = serializers.RelatedField()
    colors = serializers.RelatedField(many=True)
    subtypes = serializers.RelatedField(many=True)

    class Meta:
        model = models.Card


class LimitedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = ('id', 'name', 'text')


class DeckCardSerializer(serializers.ModelSerializer):
    card = CardSerializer()

    class Meta:
        model = models.DeckCard
        fields = ('card', 'count')


class DeckSerializer(serializers.ModelSerializer):
    cards = DeckCardSerializer(many=True)

    class Meta:
        model = models.Deck
        fields = ('id', 'title', 'private', 'user', 'cards')
