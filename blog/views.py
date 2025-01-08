from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        # Получаем только активные объекты
        return Article.objects.filter(is_published=True)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "blog/article_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "content", "preview", "is_published", "views"]
    template_name = "blog/article_form.html"
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ["title", "content", "preview", "is_published", "views"]
    template_name = "blog/article_form.html"
    success_url = reverse_lazy("blog:article_detail")

    def get_success_url(self):
        return reverse("blog:article_detail", args=[self.kwargs.get("pk")])


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:article_list")
