# Generated by Django 5.1.3 on 2025-01-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["price"],
                "permissions": [("can_unpublish_product", "Can unpublish product")],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="publish_product",
            field=models.BooleanField(default=False),
        ),
    ]
