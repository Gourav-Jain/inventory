from django import forms

class InvoiceForm(forms.Form):
    clients = forms.CharField(max_length=255, required=False)
    clientname = forms.CharField(max_length=255,required=False)
    invoiceno = forms.CharField(max_length=255,required=False)
    invoicedate = forms.CharField(max_length=255, required=False)
    duedate = forms.CharField(max_length=255, required=False)
    pono = forms.CharField(max_length=255,required=False)
    itemid = forms.CharField(max_length=255,required=False)
    itemname = forms.CharField(max_length=255,required=False)
    hsn = forms.CharField(max_length=255,required=False)
    unit = forms.CharField(max_length=255,required=False)
    qty = forms.CharField(max_length=255,required=False)
    price = forms.CharField(max_length=255,required=False)
    disc =  forms.CharField(max_length=255,required=False)
    gst = forms.CharField(max_length=255,required=False)
    itemtotal = forms.CharField(max_length=255,required=False)
    subtotal = forms.CharField(max_length=255,required=False)
    taxtotal = forms.CharField(max_length=255,required=False)
    disctotal = forms.CharField(max_length=255,required=False)
    total = forms.CharField(max_length=255,required=False)


class ClientsForm(forms.Form):
    clientname = forms.CharField()
    billto = forms.CharField()
    shipto = forms.CharField(required=False)
    issame =  forms.BooleanField()
    email = forms.EmailField()
    contactnum = forms.CharField()
    
class ProductsForm(forms.Form):
    productname = forms.CharField()
    tax = forms.IntegerField()
    unit = forms.CharField()
    hsn = forms.CharField()
    price = forms.DecimalField()
    