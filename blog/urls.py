from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


app_name = BlogConfig.name


urlpatterns = [
    path('blog/', ArticleListView.as_view(), name='article_list'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('blog/create', ArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('blog/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
