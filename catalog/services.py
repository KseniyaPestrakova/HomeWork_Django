from catalog.models import Product, Category


def category_products(category_id):
    filter_products = Product.objects.filter(category=Category.objects.get(pk=category_id))
    return filter_products
