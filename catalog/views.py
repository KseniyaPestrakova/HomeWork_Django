from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductsHomeListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product


class ProductsTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/contacts.html'
    context_object_name = 'product'
