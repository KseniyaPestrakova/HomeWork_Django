from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок публикации")
    content = models.TextField(blank=True, null=True)
    preview = models.ImageField(upload_to="media/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = ["created_at"]
