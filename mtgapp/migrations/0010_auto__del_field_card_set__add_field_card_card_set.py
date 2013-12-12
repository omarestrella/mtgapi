# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Card.set'
        db.delete_column(u'mtgapp_card', 'set_id')

        # Adding field 'Card.card_set'
        db.add_column(u'mtgapp_card', 'card_set',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtgapp.CardSet'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Card.set'
        db.add_column(u'mtgapp_card', 'set',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtgapp.CardSet'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Card.card_set'
        db.delete_column(u'mtgapp_card', 'card_set_id')


    models = {
        u'mtgapp.card': {
            'Meta': {'object_name': 'Card'},
            'card_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mtgapp.CardSet']", 'null': 'True', 'blank': 'True'}),
            'cmc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mtgapp.CardColor']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layout': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'subtypes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'card'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mtgapp.CardSubtype']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'toughness': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'card'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mtgapp.CardType']"})
        },
        u'mtgapp.cardcolor': {
            'Meta': {'object_name': 'CardColor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mtgapp.cardset': {
            'Meta': {'object_name': 'CardSet'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'release_date': ('django.db.models.fields.DateField', [], {})
        },
        u'mtgapp.cardsubtype': {
            'Meta': {'object_name': 'CardSubtype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mtgapp.cardtype': {
            'Meta': {'object_name': 'CardType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['mtgapp']