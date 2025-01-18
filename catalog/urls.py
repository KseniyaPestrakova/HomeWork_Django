from django.urls import path

from .views import ProductsDetailView, ProductsHomeListView, ProductsTemplateView, ProductsCreateView, \
    ProductsUpdateView, ProductsDeleteView, UnpublishProductView, CategoryProductsListView

app_name = "catalog"

urlpatterns = [
    path("", ProductsHomeListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductsDetailView.as_view(), name="product_detail"),
    path("contacts/", ProductsTemplateView.as_view(), name="contacts"),
    path("products/create/", ProductsCreateView.as_view(), name="product_create"),
    path("products/update/<int:pk>/", ProductsUpdateView.as_view(), name="product_update"),
    path("products/delete/<int:pk>/", ProductsDeleteView.as_view(), name="product_confirm_delete"),
    path("products/unpublish/<int:pk>/", UnpublishProductView.as_view(), name="product_unpublish"),
    path("category/<int:pk>/", CategoryProductsListView.as_view(), name="category_products"),
]
