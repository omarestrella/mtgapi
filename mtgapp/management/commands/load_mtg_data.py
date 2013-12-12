import os
import json

from django.core.management.base import BaseCommand

from mtgapp import models

DIR = os.path.dirname(os.path.abspath(__file__))

ALL_CARDS = '%s/../../../seed_data/data/all_cards.json' % DIR
META = '%s/../../../seed_data/data/meta.json' % DIR
SETS = '%s/../../../seed_data/data/sets.json' % DIR


def fields_for_model(cls):
    fields = cls._meta.fields
    return [f.attname for f in fields if f.attname != 'id']


def intersection(keys, data):
    return dict((k, data[k]) for k in keys if k in data)


class Command(BaseCommand):
    @staticmethod
    def clean_data():
        models.CardColor.objects.all().delete()
        models.CardSet.objects.all().delete()
        models.CardType.objects.all().delete()
        models.CardSubtype.objects.all().delete()
        models.Card.objects.all().delete()

    @staticmethod
    def handle_meta(data):
        types = data.get('types')
        subtypes = data.get('subtypes')
        colors = data.get('colors')

        [models.CardType.objects.create(name=t) for t in types]
        [models.CardSubtype.objects.create(name=st) for st in subtypes]
        [models.CardColor.objects.create(name=c) for c in colors]

    @staticmethod
    def handle_sets(data):
        sets = data.get('sets')
        [models.CardSet.objects.create(**s) for s in sets]

    @staticmethod
    def handle_cards(data):
        default_card_keys = ['name', 'cmc', 'layout', 'power', 'toughness', 'text']
        for name, card in data.iteritems():
            colors = models.CardColor.objects.filter(name__in=card.get('colors'))
            types = models.CardType.objects.filter(name__in=card.get('types'))
            subtypes = models.CardSubtype.objects.filter(name__in=card.get('subtypes', []))
            card_set = models.CardSet.objects.get(code=card.get('set'))

            default_data = intersection(default_card_keys, card)
            default_data.update({
                'card_set': card_set,
                'type_name': card['type'],
                'image_name': card['imageName']
            })

            card = models.Card.objects.create(**default_data)
            card.colors.add(*colors)
            card.types.add(*types)
            card.subtypes.add(*subtypes)
            card.save()


    def handle(self, *args, **options):
        self.clean_data()

        all_cards = file(ALL_CARDS, 'r')
        meta = file(META, 'r')
        sets = file(SETS, 'r')

        all_cards_data = json.load(all_cards)
        meta_data = json.load(meta)
        sets_data = json.load(sets)

        self.handle_meta(meta_data)
        self.handle_sets(sets_data)
        self.handle_cards(all_cards_data);
