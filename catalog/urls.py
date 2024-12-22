from django.urls import path
from . import views
from .views import home, product_detail

app_name = "catalog"

urlpatterns = [path('', home, name="home"),
               path('products/<int:pk>/', product_detail, name="product_detail"),
               path("contacts/", views.contacts, name="contacts"),
               ]
