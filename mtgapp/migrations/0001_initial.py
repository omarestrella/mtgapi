# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CardSet'
        db.create_table(u'mtgapp_cardset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('block', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'mtgapp', ['CardSet'])

        # Adding model 'CardType'
        db.create_table(u'mtgapp_cardtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mtgapp', ['CardType'])

        # Adding model 'CardSubtype'
        db.create_table(u'mtgapp_cardsubtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mtgapp', ['CardSubtype'])

        # Adding model 'CardColor'
        db.create_table(u'mtgapp_cardcolor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mtgapp', ['CardColor'])

        # Adding model 'Card'
        db.create_table(u'mtgapp_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtgapp.CardSet'])),
            ('cmc', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('layout', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('power', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
            ('toughness', self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True)),
        ))
        db.send_create_signal(u'mtgapp', ['Card'])

        # Adding M2M table for field types on 'Card'
        m2m_table_name = db.shorten_name(u'mtgapp_card_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'mtgapp.card'], null=False)),
            ('cardtype', models.ForeignKey(orm[u'mtgapp.cardtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'cardtype_id'])

        # Adding M2M table for field subtypes on 'Card'
        m2m_table_name = db.shorten_name(u'mtgapp_card_subtypes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'mtgapp.card'], null=False)),
            ('cardsubtype', models.ForeignKey(orm[u'mtgapp.cardsubtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'cardsubtype_id'])

        # Adding M2M table for field colors on 'Card'
        m2m_table_name = db.shorten_name(u'mtgapp_card_colors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'mtgapp.card'], null=False)),
            ('cardcolor', models.ForeignKey(orm[u'mtgapp.cardcolor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'cardcolor_id'])


    def backwards(self, orm):
        # Deleting model 'CardSet'
        db.delete_table(u'mtgapp_cardset')

        # Deleting model 'CardType'
        db.delete_table(u'mtgapp_cardtype')

        # Deleting model 'CardSubtype'
        db.delete_table(u'mtgapp_cardsubtype')

        # Deleting model 'CardColor'
        db.delete_table(u'mtgapp_cardcolor')

        # Deleting model 'Card'
        db.delete_table(u'mtgapp_card')

        # Removing M2M table for field types on 'Card'
        db.delete_table(db.shorten_name(u'mtgapp_card_types'))

        # Removing M2M table for field subtypes on 'Card'
        db.delete_table(db.shorten_name(u'mtgapp_card_subtypes'))

        # Removing M2M table for field colors on 'Card'
        db.delete_table(db.shorten_name(u'mtgapp_card_colors'))


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
            'block': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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