from django.conf.urls.defaults import *

urlpatterns = patterns('invoicer.views',
    url(r'invoices/(?P<id>[\w-]+)/edit$', 'edit_invoice', name="edit_invoice"),
    url(r'invoices/(?P<id>[\w-]+)/add_line$', 'add_line', name="add_line"),
    url(r'invoices/(?P<id>[\w-]+)$', 'view_invoice', name="invoice"),
    url(r'company/(?P<id>[\d]+)/$', 'company_overview', name="company"),
    url(r'client/(?P<id>[\d]+)/$', 'client_overview', name="client"),
    url(r'company/(?P<id>[\d]+)/invoices/(?P<page>[\d]*)$', 'company_invoices', name="company_invoices"),
    url(r'client/(?P<id>[\d]+)/invoices/(?P<page>[\d]*)$', 'client_invoices', name="client_invoices"),
)
