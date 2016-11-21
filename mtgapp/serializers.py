from rest_framework import pagination
from rest_framework_json_api import serializers, relations
# from rest_framework_json_api.relations import ResourceRelatedField

from mtgapp import models


class CardSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardSet
        fields = '__all__'


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardType
        fields = '__all__'


class CardColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardColor
        fields = '__all__'


class CardSubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CardSubtype
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    sets = relations.ResourceRelatedField(queryset=models.CardSet.objects, many=True)
    types = relations.ResourceRelatedField(queryset=models.CardType.objects, many=True)
    colors = relations.ResourceRelatedField(queryset=models.CardColor.objects, many=True)
    subtypes = relations.ResourceRelatedField(queryset=models.CardSubtype.objects, many=True)

    class Meta:
        model = models.Card
        fields = '__all__'


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
    included_serializers = {
        'cards': DeckCardSerializer
    }

    def create(self, validated_data):
        cards = validated_data.pop('cards')
        deck = models.Deck.objects.create(**validated_data)
        if cards:
            deck.cards.add(*cards)
            deck.save()
        return deck


    class Meta:
        model = models.Deck
        fields = ('id', 'title', 'private', 'user', 'cards')
