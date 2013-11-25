from django.contrib import admin

from mtgapp import models


admin.site.register(models.Card)
admin.site.register(models.CardColor)
admin.site.register(models.CardType)
admin.site.register(models.CardSubtype)
admin.site.register(models.CardSet)

