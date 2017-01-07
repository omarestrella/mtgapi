from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CardSet(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)
    block = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField()

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.code)


class CardType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{}'.format(self.name)

class CardSubtype(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{}'.format(self.name)

class CardColor(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Card(models.Model):
    LAYOUT_CHOICES = (
        ('split', 'Split'),
        ('normal', 'Normal')
    )

    RARITY_CHOICES = (
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('mythic', 'Mythic Rare')
    )

    name = models.CharField(max_length=255)
    text = models.TextField()
    cmc = models.PositiveSmallIntegerField(blank=True, null=True)
    type_name = models.CharField(max_length=255)
    types = models.ManyToManyField(CardType, blank=True, related_name='card')
    subtypes = models.ManyToManyField(CardSubtype, blank=True, related_name='card')
    colors = models.ManyToManyField(CardColor, blank=True)
    sets = models.ManyToManyField(CardSet, blank=True, related_name='card')
    layout = models.CharField(max_length=255, choices=LAYOUT_CHOICES)
    power = models.CharField(max_length=3, blank=True, null=True)
    toughness = models.CharField(max_length=3, blank=True, null=True)
    image_name = models.CharField(max_length=255)
    multiverse_id = models.IntegerField()
    set_number = models.CharField(max_length=255, blank=True, null=True)

    @property
    def is_equipment(self):
        return False

    def __unicode__(self):
        return u'{}'.format(self.name)


class Deck(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    private = models.BooleanField(default=False)

    def __unicode__(self):
        return u'{} by {}'.format(self.title, self.user.username)


class DeckCard(models.Model):
    card = models.ForeignKey(Card)
    count = models.PositiveSmallIntegerField()
    deck = models.ForeignKey(Deck, related_name='cards')


class Game(models.Model):
    users = models.ManyToManyField(User)
    decks = models.ManyToManyField(Deck)
