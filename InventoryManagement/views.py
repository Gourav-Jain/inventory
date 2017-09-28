from django.shortcuts import render, redirect, render_to_response
from .models import Clients
from django.http import JsonResponse
from InventoryManagement.models import Products, Invoices, InvoiceProducts, Clients
from .forms import InvoiceForm, ClientsForm, ProductsForm
from _operator import inv

# Create your views here.
def index(request):
    return render(request, 'template/index.html')


def invoice(request):
    if(request.method == "POST"):
        print("")
    elif(request.method == "GET"):
        invoiceno = Invoices.objects.all().order_by("-id")[0]
        newnum = invoiceno.id + 1
        all_clients = Clients.objects.values("id","name")
        all_products = Products.objects.values("id","name", "price")
        return render(request, 'template/invoice.html', {'clients':all_clients, 'products': all_products, 'innumber':newnum})
    else:
        print("Not found")
    return render(request, 'template/invoice.html')

def invoicepreview(request):
    tabledata = []
    data = request.POST
    if(request.method == "POST"):
        invform = InvoiceForm(request.POST)
        if (invform.is_valid()):
            invform.clientname = invform.cleaned_data["clientname"]
            invform.clients = invform.cleaned_data["clients"]
            invform.invoiceno = invform.cleaned_data["invoiceno"]
            invform.invoicedate = invform.cleaned_data["invoicedate"]
            invform.duedate = invform.cleaned_data["duedate"]
           
            
            
            invform.subtotal = invform.cleaned_data["subtotal"]
            invform.taxtotal = invform.cleaned_data["taxtotal"]
            invform.disctotal = invform.cleaned_data["disctotal"]
            invform.total = invform.cleaned_data["total"]
            
            oInvoice = Invoices()
            oInvoice.number = invform.invoiceno
            oInvoice.due_date = invform.duedate
            oInvoice.issue_date = invform.invoicedate
            oInvoice.total_tax = invform.taxtotal
            oInvoice.total_all = invform.total
            oInvoice.total_no_tax = invform.subtotal
            oInvoice.discount = invform.disctotal
            oInvoice.client_id = invform.clients
            oInvoice.client_name = invform.clientname
            oInvoice.layout = 1
            oInvoice.print_id = 0
            oInvoice.esugam_label = 0
            oInvoice.save()
            
            invform.itemid = request.POST.getlist("itemname") #comma sepreted value
            invform.itemname = request.POST.getlist("hdnitemname") #comma sepreted value
            invform.hsn = request.POST.getlist("hsn")
            invform.unit = request.POST.getlist("unit") 
            invform.qty = request.POST.getlist("qty")            
            invform.price = request.POST.getlist("price")
            invform.disc = request.POST.getlist("disc")
            invform.gst = request.POST.getlist("gst")
            invform.itemtotal = request.POST.getlist("itemtotal")
            
            for idx, val in enumerate(invform.itemid):
                oInvProd = InvoiceProducts()
                oInvProd.product_id = val
                oInvProd.invoice_id = invform.invoiceno
                oInvProd.name = invform.itemname[idx]
                oInvProd.hsn = invform.hsn[idx] if invform.hsn[idx] != '' else 0 
                oInvProd.quantity = invform.qty[idx] if invform.qty[idx] != '' else 1
                oInvProd.measuring_unit = invform.unit[idx] if invform.unit[idx] != '' else 0
                oInvProd.price = invform.price[idx]
                oInvProd.discount_percentage = invform.disc[idx] if invform.disc[idx] != '' else 0
                oInvProd.tax_id = invform.gst[idx]
                oInvProd.total_all = invform.itemtotal[idx]
                tabledata.append(oInvProd)
                oInvProd.save()
            
            #return render_to_response('template/invoicepreview.html')
        else:
            print("")    
    return render(request, "template/invoicepreview.html", {"form":data, "tbl":tabledata})

def get_item_details(request):
    itemid = request.GET.get('itemid', None)
    data = {'price': getpricebyid(itemid)}
    return JsonResponse(data)

def getpricebyid(itemid):
    data = Products.objects.filter(id=itemid).values_list('price',flat=True)[0]
    return data

def clients(request):
    if(request.method == "POST"):
        oformClient =  ClientsForm(request.POST)
        if(oformClient.is_valid()):
            oformClient.clientname = oformClient.cleaned_data["clientname"]
            oformClient.billto = oformClient.cleaned_data["billto"]
            oformClient.shipto = oformClient.cleaned_data["shipto"]
            oformClient.contactnum = oformClient.cleaned_data["contactnum"]
            oformClient.issame = oformClient.cleaned_data["issame"]
            oformClient.email = oformClient.cleaned_data["email"]
            
            
            oClient = Clients()
            oClient.name = oformClient.clientname
            oClient.billing_address = oformClient.billto
            oClient.shipping_address = oformClient.shipto
            oClient.contact = oformClient.contactnum
            oClient.email = oformClient.email
            oClient.save()
        else:
            print("error in validation")
    else:
        print()
    return render(request, 'template/clients.html')

def products(request):
    if(request.method == "POST"):
        oformProd = ProductsForm(request.POST)
        if(oformProd.is_valid()):
            oformProd.productname = oformProd.cleaned_data["productname"]
            oformProd.tax = oformProd.cleaned_data["tax"]
            oformProd.unit = oformProd.cleaned_data["unit"]
            oformProd.hsn = oformProd.cleaned_data["hsnnumber"]
            oformProd.price = oformProd.cleaned_data["price"]
            
            oProd = Products()
            oProd.name = oformProd.productname
            oProd.measuring_unit = oformProd.unit
            oProd.hsn = oformProd.hsn
            oProd.tax_id = oformProd.tax
            oProd.price = oformProd.price            
            oProd.save();
            
        else:
            print("error in validation")
    else:
        print()
    return render(request, 'template/products.html')