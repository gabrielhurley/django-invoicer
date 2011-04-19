# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('invoicer_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=80, blank=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
        ))
        db.send_create_signal('invoicer', ['Client'])

        # Adding model 'Company'
        db.create_table('invoicer_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=80, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('numbering_prefix', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('billing_email', self.gf('django.db.models.fields.EmailField')(max_length=80, blank=True)),
            ('tax_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('invoicer', ['Company'])

        # Adding model 'Terms'
        db.create_table('invoicer_terms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=256)),
        ))
        db.send_create_signal('invoicer', ['Terms'])

        # Adding model 'LineItem'
        db.create_table('invoicer_lineitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('taxable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(related_name='line_items', to=orm['invoicer.Invoice'])),
        ))
        db.send_create_signal('invoicer', ['LineItem'])

        # Adding model 'Invoice'
        db.create_table('invoicer_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invoices', to=orm['invoicer.Company'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='invoices', to=orm['invoicer.Client'])),
            ('invoice_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('invoice_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('status_notes', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('terms', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['invoicer.Terms'])),
        ))
        db.send_create_signal('invoicer', ['Invoice'])

        # Adding model 'Stylesheet'
        db.create_table('invoicer_stylesheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stylesheets', to=orm['invoicer.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('stylesheet', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('introduction_text', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
            ('feedback_text', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
            ('misc_text', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
            ('thank_you_text', self.gf('django.db.models.fields.TextField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('invoicer', ['Stylesheet'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('invoicer_client')

        # Deleting model 'Company'
        db.delete_table('invoicer_company')

        # Deleting model 'Terms'
        db.delete_table('invoicer_terms')

        # Deleting model 'LineItem'
        db.delete_table('invoicer_lineitem')

        # Deleting model 'Invoice'
        db.delete_table('invoicer_invoice')

        # Deleting model 'Stylesheet'
        db.delete_table('invoicer_stylesheet')


    models = {
        'invoicer.client': {
            'Meta': {'object_name': 'Client'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'invoicer.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'billing_email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '80', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numbering_prefix': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'tax_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'invoicer.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': "orm['invoicer.Client']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': "orm['invoicer.Company']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status_notes': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['invoicer.Terms']"})
        },
        'invoicer.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'line_items'", 'to': "orm['invoicer.Invoice']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'taxable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'invoicer.stylesheet': {
            'Meta': {'object_name': 'Stylesheet'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stylesheets'", 'to': "orm['invoicer.Company']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'feedback_text': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction_text': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'misc_text': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'stylesheet': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'thank_you_text': ('django.db.models.fields.TextField', [], {'max_length': '256', 'blank': 'True'})
        },
        'invoicer.terms': {
            'Meta': {'object_name': 'Terms'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['invoicer']
