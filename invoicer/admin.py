from django.contrib import admin

from invoicer.models import *

class LineItemInline(admin.TabularInline):
    model = LineItem
    fields = ("item", "name", "cost", "price", "quantity", "taxable")

class InvoiceInline(admin.TabularInline):
    fields = ("invoice_date", "status", "due_date", "company", )
    readonly_fields = ("invoice_date", "due_date", "company",)
    model = Invoice
    max_num = 0
    extra = 0
    
class StylesheetInline(admin.StackedInline):
    model = Stylesheet
    extra = 1
    max_num = 1

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("name", "numbering_prefix", "billing_email", "tax_rate"),
        },),
        ("Contact Info", {
            "fields": ("contact_person", "phone_number", "email", "website"),
        },),
        ("Address", {
            "fields": ("address", "city", "state", "zip_code",), "classes": ("wide",)
        },),
    )
    model = Company
    inlines = (StylesheetInline,)

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ("name", "email", "phone_number", "full_address", "receipts_to_date")
    inlines = (InvoiceInline,)
    
class TermsAdmin(admin.ModelAdmin):
    model = Terms
    
class InvoiceAdmin(admin.ModelAdmin):
    model = Invoice
    list_display = ("invoice_number", "client", "company", "invoice_date", "due_date", "status",)
    list_filter = ("client", "company", "invoice_date", "due_date", "status",)
    list_editable = ("status",)
    search_fields = ("invoice_number",)
    fieldsets = (
        (None, {"fields": (("company", "invoice_date",), ("client", "due_date",), "terms", ("status", "status_notes",), "invoice_number",)}),
    )
    inlines = (LineItemInline,)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Item)
