# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DeckCard'
        db.create_table(u'mtgapp_deckcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtgapp.Card'])),
            ('count', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('deck', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cards', to=orm['mtgapp.Deck'])),
        ))
        db.send_create_signal(u'mtgapp', ['DeckCard'])

        # Removing M2M table for field cards on 'Deck'
        db.delete_table(db.shorten_name(u'mtgapp_deck_cards'))


    def backwards(self, orm):
        # Deleting model 'DeckCard'
        db.delete_table(u'mtgapp_deckcard')

        # Adding M2M table for field cards on 'Deck'
        m2m_table_name = db.shorten_name(u'mtgapp_deck_cards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('deck', models.ForeignKey(orm[u'mtgapp.deck'], null=False)),
            ('card', models.ForeignKey(orm[u'mtgapp.card'], null=False))
        ))
        db.create_unique(m2m_table_name, ['deck_id', 'card_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mtgapp.card': {
            'Meta': {'object_name': 'Card'},
            'card_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mtgapp.CardSet']", 'null': 'True', 'blank': 'True'}),
            'cmc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mtgapp.CardColor']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'layout': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'multiverse_id': ('django.db.models.fields.IntegerField', [], {}),
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
        },
        u'mtgapp.deck': {
            'Meta': {'object_name': 'Deck'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mtgapp.deckcard': {
            'Meta': {'object_name': 'DeckCard'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mtgapp.Card']"}),
            'count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'deck': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cards'", 'to': u"orm['mtgapp.Deck']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mtgapp']