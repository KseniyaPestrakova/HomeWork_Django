from django.shortcuts import render, get_object_or_404

from catalog.models import Product

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MyProductsHomeListView(ListView):
    model = Product
    template_name = 'catalog/home_list.html'
    context_object_name = 'mymodels'


def home(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "GET":
        return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)

