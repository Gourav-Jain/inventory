from django.conf.urls import url
from . import views

#create URL patterns here
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^invoice$', views.invoice, name='invoice'),
    url(r'^invoicep$', views.invoicepreview, name='invoicep'),
    url(r'^clients$', views.clients, name='clients'),
    url(r'^products$', views.products, name='products'),
    url(r'^get_item_details$', views.get_item_details, name="get_item_details")
    ]