from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class ProductsHomeListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product


class ProductsTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"
    context_object_name = "product"
