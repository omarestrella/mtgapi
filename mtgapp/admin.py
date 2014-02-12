from django.contrib import admin

from mtgapp import models


class CardAdmin(admin.ModelAdmin):
    search_fields = ['name', 'text']


admin.site.register(models.Card, CardAdmin)
admin.site.register(models.CardColor)
admin.site.register(models.CardType)
admin.site.register(models.CardSubtype)
admin.site.register(models.CardSet)


class DeckCardInline(admin.StackedInline):
    model = models.DeckCard


class DeckAdmin(admin.ModelAdmin):
    inlines = [
        DeckCardInline
    ]

admin.site.register(models.Deck, DeckAdmin)
