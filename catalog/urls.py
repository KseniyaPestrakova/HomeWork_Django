from django.urls import path
from .views import ProductsHomeListView, ProductsDetailView, ProductsTemplateView

app_name = "catalog"

urlpatterns = [path('', ProductsHomeListView.as_view(), name="product_list"),
               path('products/<int:pk>/', ProductsDetailView.as_view(), name="product_detail"),
               path("contacts/", ProductsTemplateView.as_view(), name="contacts"),
               ]
