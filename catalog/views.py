from django.views.generic import DetailView, ListView, TemplateView, UpdateView, DeleteView, View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

from catalog.services import category_products


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        product.publish_product = False
        product.save()

        return redirect('catalog:product_list')


class ProductsHomeListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 5)
        return queryset


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductsTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"
    context_object_name = "product"


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user
        if product.owner == user or user.has_perm('catalog.can_unpublish_product'):
            return product
        else:
            raise PermissionDenied


class CategoryProductsListView(ListView):
    model = Category
    template_name = "catalog/category_products.html"

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        queryset = category_products(category_id=category_id)
        return queryset
