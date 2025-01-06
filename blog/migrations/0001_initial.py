# Generated by Django 5.1.3 on 2025-01-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogArticle",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=300, verbose_name="Заголовок публикации")),
                ("content", models.TextField(blank=True, null=True)),
                ("preview", models.ImageField(blank=True, null=True, upload_to="media/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_published", models.BooleanField(default=False)),
                ("views", models.IntegerField()),
            ],
            options={
                "verbose_name": "публикация",
                "verbose_name_plural": "публикации",
                "ordering": ["views"],
            },
        ),
    ]