from django.urls import path

from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView

app_name = "blog"

urlpatterns = [
    path("blog/", ArticleListView.as_view(), name="article_list"),
    path("blog/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("blog/create/", ArticleCreateView.as_view(), name="article_create"),
    path("blog/update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update"),
    path("blog/delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_confirm_delete"),
]
