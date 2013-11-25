# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CardSet.block'
        db.alter_column(u'mtgapp_cardset', 'block', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CardSet.block'
        raise RuntimeError("Cannot reverse this migration. 'CardSet.block' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CardSet.block'
        db.alter_column(u'mtgapp_cardset', 'block', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'mtgapp.card': {
            'Meta': {'object_name': 'Card'},
            'cmc': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mtgapp.CardColor']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mtgapp.CardSet']"}),
            'subtypes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subtypes'", 'symmetrical': 'False', 'to': u"orm['mtgapp.CardSubtype']"}),
            'toughness': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'types'", 'symmetrical': 'False', 'to': u"orm['mtgapp.CardType']"})
        },
        u'mtgapp.cardcolor': {
            'Meta': {'object_name': 'CardColor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mtgapp.cardset': {
            'Meta': {'object_name': 'CardSet'},
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
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