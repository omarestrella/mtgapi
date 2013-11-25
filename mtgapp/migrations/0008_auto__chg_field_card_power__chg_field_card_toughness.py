# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Card.power'
        db.alter_column(u'mtgapp_card', 'power', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Card.toughness'
        db.alter_column(u'mtgapp_card', 'toughness', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

    def backwards(self, orm):

        # Changing field 'Card.power'
        db.alter_column(u'mtgapp_card', 'power', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

        # Changing field 'Card.toughness'
        db.alter_column(u'mtgapp_card', 'toughness', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    models = {
        u'mtgapp.card': {
            'Meta': {'object_name': 'Card'},
            'cmc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mtgapp.CardColor']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layout': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mtgapp.CardSet']", 'null': 'True', 'blank': 'True'}),
            'subtypes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'card'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mtgapp.CardSubtype']"}),
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