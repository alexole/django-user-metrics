# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'MetricWeek'
        db.delete_table('user_metrics_metricweek')

        # Deleting field 'MetricItem.count'
        db.delete_column('user_metrics_metricitem', 'count')

        # Deleting field 'MetricItem.last_visit'
        db.delete_column('user_metrics_metricitem', 'last_visit')

        # Deleting field 'MetricItem.date_up'
        db.delete_column('user_metrics_metricitem', 'date_up')

        # Adding field 'MetricItem.visit_time'
        db.add_column('user_metrics_metricitem', 'visit_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'MetricItem.visitor_hash'
        db.add_column('user_metrics_metricitem', 'visitor_hash',
                      self.gf('django.db.models.fields.CharField')(max_length=22, null=True),
                      keep_default=False)

        # Adding field 'MetricItem.visitor_id'
        db.add_column('user_metrics_metricitem', 'visitor_id',
                      self.gf('django.db.models.fields.CharField')(max_length=22, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'MetricWeek'
        db.create_table('user_metrics_metricweek', (
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unique_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('metric', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_metrics.Metric'])),
            ('date_up', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_object_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('user_metrics', ['MetricWeek'])

        # Adding field 'MetricItem.count'
        db.add_column('user_metrics_metricitem', 'count',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'MetricItem.last_visit'
        db.add_column('user_metrics_metricitem', 'last_visit',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'MetricItem.date_up'
        db.add_column('user_metrics_metricitem', 'date_up',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today),
                      keep_default=False)

        # Deleting field 'MetricItem.visit_time'
        db.delete_column('user_metrics_metricitem', 'visit_time')

        # Deleting field 'MetricItem.visitor_hash'
        db.delete_column('user_metrics_metricitem', 'visitor_hash')

        # Deleting field 'MetricItem.visitor_id'
        db.delete_column('user_metrics_metricitem', 'visitor_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'user_metrics.metric': {
            'Meta': {'object_name': 'Metric'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'user_metrics.metricday': {
            'Meta': {'object_name': 'MetricDay'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_up': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_metrics.Metric']"}),
            'unique_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user_object_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'user_metrics.metricitem': {
            'Meta': {'object_name': 'MetricItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_metrics.Metric']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user_object_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visit_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'visitor_hash': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True'}),
            'visitor_id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True'})
        }
    }

    complete_apps = ['user_metrics']