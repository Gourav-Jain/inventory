# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AliasEmail(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    alias = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alias_email'


class BillPayments(models.Model):
    id = models.IntegerField(primary_key=True)
    payment_id = models.IntegerField(blank=True, null=True)
    bill_id = models.IntegerField(blank=True, null=True)
    amount = models.TextField()  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bill_payments'


class BillProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    bill_id = models.IntegerField(blank=True, null=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    measuring_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    quantity = models.TextField()  # This field type is a guess.
    has_tax_included = models.NullBooleanField()
    tax_id = models.IntegerField(blank=True, null=True)
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_discount = models.NullBooleanField()
    discount_percentage = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_rate = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bill_products'


class Bills(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.TextField()  # This field type is a guess.
    issue_date = models.TextField()  # This field type is a guess.
    due_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_details_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    vendor_name = models.TextField()  # This field type is a guess.
    vendor_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_paid = models.NullBooleanField()
    is_draft = models.NullBooleanField()
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    internal_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    bill_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    color = models.TextField()  # This field type is a guess.
    po_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    page_size_id = models.IntegerField(blank=True, null=True)
    vendor_billing_state_id = models.IntegerField(blank=True, null=True)
    vendor_shipping_state_id = models.IntegerField(blank=True, null=True)
    pay_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    pay_online = models.NullBooleanField()
    flag_id = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField()
    discount = models.TextField(blank=True, null=True)  # This field type is a guess.
    sent = models.NullBooleanField()
    print_id = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    fiscal_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    number_prefix = models.TextField(blank=True, null=True)  # This field type is a guess.
    second_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    excise_duty = models.TextField(blank=True, null=True)  # This field type is a guess.
    use_transport = models.NullBooleanField()
    delivery_note = models.TextField(blank=True, null=True)  # This field type is a guess.
    vehicle_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    esugam = models.TextField(blank=True, null=True)  # This field type is a guess.
    lr_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_method = models.TextField(blank=True, null=True)  # This field type is a guess.
    excise_cess = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelled = models.NullBooleanField()
    quantity_no_decimal = models.NullBooleanField()
    product_inline_discount = models.NullBooleanField()
    po_date = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bills'


class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    zip = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_short = models.CharField(max_length=2, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()  # This field type is a guess.
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_state_id = models.IntegerField(blank=True, null=True)
    shipping_state_id = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)  # This field type is a guess.
    details_public = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    tin = models.TextField(blank=True, null=True)  # This field type is a guess.
    pan = models.TextField(blank=True, null=True)  # This field type is a guess.
    vat_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    gstin = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'clients'


class CompanyDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()  # This field type is a guess.
    address = models.TextField()  # This field type is a guess.
    zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField()  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    website = models.TextField(blank=True, null=True)  # This field type is a guess.
    logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    details = models.TextField(blank=True, null=True)  # This field type is a guess.
    state_id = models.IntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    tin = models.TextField(blank=True, null=True)  # This field type is a guess.
    pan = models.TextField(blank=True, null=True)  # This field type is a guess.
    stn = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_label = models.IntegerField()
    service_category = models.ForeignKey('ServiceTaxServices', models.DO_NOTHING, blank=True, null=True)
    gstin = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_id_label = models.IntegerField()
    taxation_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_details'


class Config(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    config_id = models.IntegerField()
    key = models.CharField(db_column='KEY', max_length=50)  # Field name made lowercase.
    value = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'config'


class Currencies(models.Model):
    id = models.IntegerField(primary_key=True)
    currency_symbol = models.CharField(max_length=20)
    currency_name = models.CharField(max_length=50)
    is_used = models.NullBooleanField()
    symbol = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class Estimate(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    number = models.TextField()  # This field type is a guess.
    issue_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_until = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_details_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_name = models.TextField()  # This field type is a guess.
    client_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_paid = models.NullBooleanField()
    is_draft = models.NullBooleanField()
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    internal_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    estimate_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    color = models.TextField()  # This field type is a guess.
    po_number = models.TextField()  # This field type is a guess.
    logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    page_size_id = models.IntegerField(blank=True, null=True)
    client_billing_state_id = models.IntegerField(blank=True, null=True)
    client_shipping_state_id = models.IntegerField(blank=True, null=True)
    flag_id = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField()
    discount = models.TextField(blank=True, null=True)  # This field type is a guess.
    sent = models.NullBooleanField()
    print_id = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity_no_decimal = models.NullBooleanField()
    pay_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    pay_online = models.NullBooleanField()
    hide_shipping_date = models.NullBooleanField()
    po_number_label = models.IntegerField()
    fiscal_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    po_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    gst_type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estimate'


class EstimateConversions(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    estimate_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estimate_conversions'


class EstimatePayments(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    payment_id = models.IntegerField(blank=True, null=True)
    estimate_id = models.IntegerField(blank=True, null=True)
    amount = models.TextField()  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estimate_payments'


class EstimateProducts(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    product_id = models.IntegerField(blank=True, null=True)
    estimate_id = models.IntegerField(blank=True, null=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    measuring_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    quantity = models.TextField()  # This field type is a guess.
    has_tax_included = models.NullBooleanField()
    tax_id = models.IntegerField(blank=True, null=True)
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_discount = models.NullBooleanField()
    discount_percentage = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    hsn = models.CharField(max_length=30, blank=True, null=True)
    sac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estimate_products'


class FacturiStornate(models.Model):
    id = models.IntegerField(primary_key=True)
    factura_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_stornarii = models.TextField(blank=True, null=True)
    valoare1 = models.TextField(blank=True, null=True)
    valoare2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturi_stornate'


class FiscYear(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    document_type = models.TextField()  # This field type is a guess.
    start_number = models.TextField()  # This field type is a guess.
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'fisc_year'


class Flags(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    value_with_tax = models.BooleanField()
    invoice_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    estimate_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    price_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    show_address = models.NullBooleanField()
    total_without_decimals = models.NullBooleanField()
    total_in_words = models.NullBooleanField()
    show_signature = models.NullBooleanField()
    shipping_price = models.IntegerField(blank=True, null=True)
    replace_quantity = models.NullBooleanField()
    show_shipping = models.NullBooleanField()
    shipping_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    indian_format = models.IntegerField(blank=True, null=True)
    show_up_column = models.IntegerField(blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    show_um_column = models.IntegerField(blank=True, null=True)
    show_tax_column = models.IntegerField(blank=True, null=True)
    show_tax_percentage = models.IntegerField(blank=True, null=True)
    excise_duty = models.TextField(blank=True, null=True)  # This field type is a guess.
    hide_amount = models.IntegerField(blank=True, null=True)
    um_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    tax_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    replace_paypal = models.IntegerField(blank=True, null=True)
    fisc_year_start = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_fisc_year = models.NullBooleanField()
    use_document_prefix = models.NullBooleanField()
    prefix_separator = models.TextField(blank=True, null=True)  # This field type is a guess.
    use_date_prefix = models.NullBooleanField()
    show_delivery_note_amount = models.IntegerField(blank=True, null=True)
    po_number_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    odt_activated = models.NullBooleanField()
    use_pin_code = models.NullBooleanField()
    tax_invoice_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    retail_invoice_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    excise_invoice_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    proforma_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    challan_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    show_contact_name = models.NullBooleanField()
    copy_type_original = models.TextField(blank=True, null=True)  # This field type is a guess.
    copy_type_dupl = models.TextField(blank=True, null=True)  # This field type is a guess.
    copy_type_tripl = models.TextField(blank=True, null=True)  # This field type is a guess.
    copy_type_quadr = models.TextField(blank=True, null=True)  # This field type is a guess.
    a5_more_pages = models.NullBooleanField()
    header_on_all_pages = models.NullBooleanField()
    show_net_received = models.NullBooleanField()
    use_second_number = models.NullBooleanField()
    change_dosc_df = models.NullBooleanField()
    basic_inventory = models.NullBooleanField()
    inventory_docs = models.NullBooleanField()
    rmv_product_qty_decimals = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'flags'


class InvoicePayments(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    payment_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    amount = models.TextField()  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoice_payments'


class InvoiceProducts(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    product_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    measuring_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    quantity = models.TextField()  # This field type is a guess.
    has_tax_included = models.NullBooleanField()
    tax_id = models.IntegerField(blank=True, null=True)
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_discount = models.NullBooleanField()
    discount_percentage = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    hsn = models.CharField(max_length=30, blank=True, null=True)
    sac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_products'


class Invoices(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    number = models.TextField()  # This field type is a guess.
    issue_date = models.TextField()  # This field type is a guess.
    due_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_details_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_name = models.TextField()  # This field type is a guess.
    client_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_paid = models.NullBooleanField()
    is_draft = models.NullBooleanField()
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    internal_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    invoice_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    color = models.TextField()  # This field type is a guess.
    po_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    page_size_id = models.IntegerField(blank=True, null=True)
    client_billing_state_id = models.IntegerField(blank=True, null=True)
    client_shipping_state_id = models.IntegerField(blank=True, null=True)
    pay_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    pay_online = models.NullBooleanField()
    flag_id = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField()
    discount = models.TextField(blank=True, null=True)  # This field type is a guess.
    sent = models.NullBooleanField()
    print_id = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    fiscal_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    number_prefix = models.TextField(blank=True, null=True)  # This field type is a guess.
    second_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    excise_duty = models.TextField(blank=True, null=True)  # This field type is a guess.
    use_transport = models.NullBooleanField()
    delivery_note = models.TextField(blank=True, null=True)  # This field type is a guess.
    vehicle_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    esugam = models.TextField(blank=True, null=True)  # This field type is a guess.
    lr_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_method = models.TextField(blank=True, null=True)  # This field type is a guess.
    excise_cess = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelled = models.NullBooleanField()
    quantity_no_decimal = models.NullBooleanField()
    product_inline_discount = models.NullBooleanField()
    esugam_label = models.IntegerField()
    po_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    gst_type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class PageSize(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    format = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'page_size'


class Payments(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    amount = models.TextField()  # This field type is a guess.
    type = models.TextField()  # This field type is a guess.
    note = models.TextField()  # This field type is a guess.
    pay_date = models.TextField()  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    advance = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'payments'


class Products(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    measuring_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    has_tax_included = models.BooleanField()
    tax_id = models.IntegerField(blank=True, null=True)
    deleted = models.TextField()  # This field type is a guess.
    type = models.TextField()  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    hsn = models.CharField(max_length=30, blank=True, null=True)
    sac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class PurchaseOrder(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    number = models.TextField()  # This field type is a guess.
    issue_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_until = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_details_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField(blank=True, null=True)
    vendor_name = models.TextField()  # This field type is a guess.
    vendor_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_paid = models.NullBooleanField()
    is_draft = models.NullBooleanField()
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    internal_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_order_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    color = models.TextField()  # This field type is a guess.
    po_number = models.TextField()  # This field type is a guess.
    logo = models.TextField(blank=True, null=True)  # This field type is a guess.
    page_size_id = models.IntegerField(blank=True, null=True)
    vendor_billing_state_id = models.IntegerField(blank=True, null=True)
    vendor_shipping_state_id = models.IntegerField(blank=True, null=True)
    flag_id = models.IntegerField(blank=True, null=True)
    layout = models.IntegerField()
    discount = models.TextField(blank=True, null=True)  # This field type is a guess.
    sent = models.NullBooleanField()
    print_id = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity_no_decimal = models.NullBooleanField()
    pay_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    pay_online = models.NullBooleanField()
    hide_shipping_date = models.NullBooleanField()
    po_number_label = models.IntegerField()
    fiscal_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    po_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    gst_type = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderConversions(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, blank=True, null=True)
    bill_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_conversions'


class PurchaseOrderProducts(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    product_id = models.IntegerField(blank=True, null=True)
    purchase_order_id = models.IntegerField(blank=True, null=True)
    name = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    measuring_unit = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.TextField()  # This field type is a guess.
    quantity = models.TextField()  # This field type is a guess.
    has_tax_included = models.NullBooleanField()
    tax_id = models.IntegerField(blank=True, null=True)
    total_no_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_tax = models.TextField(blank=True, null=True)  # This field type is a guess.
    total_all = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_discount = models.NullBooleanField()
    discount_percentage = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    sku = models.TextField(blank=True, null=True)  # This field type is a guess.
    purchase_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    hsn = models.CharField(max_length=30, blank=True, null=True)
    sac = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_products'


class ReleaseNotes(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    version = models.TextField()  # This field type is a guess.
    year = models.TextField()  # This field type is a guess.
    release_notes = models.TextField(blank=True, null=True)  # This field type is a guess.
    show_notes = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'release_notes'


class ServiceTaxServices(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    service_category = models.TextField()  # This field type is a guess.
    introduction_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    ac_tax_collection = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_other_receipts = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_deduct_refunds = models.TextField(blank=True, null=True)  # This field type is a guess.
    ac_education_cess = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'service_tax_services'


class States(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    tin = models.CharField(max_length=5, blank=True, null=True)
    state_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class Stocks(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    sold_quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    sold_total_amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    cogs = models.TextField(blank=True, null=True)  # This field type is a guess.
    gross_margin = models.TextField(blank=True, null=True)  # This field type is a guess.
    gross_margin_percent = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'stocks'


class TaxCombo(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    main_tax_id = models.IntegerField(blank=True, null=True)
    component_tax_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_combo'


class Taxes(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    tax_name = models.CharField(max_length=50)
    tax_percentage = models.TextField()  # This field type is a guess.
    is_default_tax = models.NullBooleanField()
    deleted = models.CharField(max_length=1, blank=True, null=True)
    tax_on_taxable_value = models.NullBooleanField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    explicit_order = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'taxes'


class Tips(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    text = models.TextField(blank=True, null=True)  # This field type is a guess.
    priority = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tips'


class Vendors(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.TextField()  # This field type is a guess.
    code = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    telephone = models.TextField(blank=True, null=True)  # This field type is a guess.
    contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_zip = models.TextField(blank=True, null=True)  # This field type is a guess.
    shipping_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    billing_state_id = models.IntegerField(blank=True, null=True)
    shipping_state_id = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)  # This field type is a guess.
    details_public = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted = models.TextField()  # This field type is a guess.
    tin = models.TextField(blank=True, null=True)  # This field type is a guess.
    pan = models.TextField(blank=True, null=True)  # This field type is a guess.
    vendor_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    vat_number = models.TextField(blank=True, null=True)  # This field type is a guess.
    gstin = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vendors'


class Version(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50)
    year = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'version'
