from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
from catalog.models import Product


class ProductsHomeListView(ListView):
    model = Product


class ProductsDetailView(LoginRequiredMixin,DetailView):
    model = Product


class ProductsTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"
    context_object_name = "product"


class ProductsCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductsUpdateView(LoginRequiredMixin,UpdateView):
    model = Product  # Указываем модель, с которой будет работать это представление
    form_class = ProductForm  # Указываем форму, которая будет использоваться для ввода данных
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductsDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

