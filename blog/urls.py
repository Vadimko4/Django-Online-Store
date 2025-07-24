from django.urls import path

from blog.apps import BlogConfig
from blog.views import RecordDetailView, RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView


app_name = BlogConfig


urlpatterns = [
    path('blog/', RecordListView.as_view(), name='record_list'),
    path('blog/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('blog/create', RecordCreateView.as_view(), name='record_create'),
    path('blog/<int:pk>/update/', RecordUpdateView.as_view(), name='record_update'),
    path('blog/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),
]
