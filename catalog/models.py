from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Продукт")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, default="", blank=True, null=True, related_name="products"
    )
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_product = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
