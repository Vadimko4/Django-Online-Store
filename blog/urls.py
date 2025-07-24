from django.urls import path

from blog.apps import BlogConfig
from blog.views import RecordDetailView, RecordListView, RecordCreateView


app_name = BlogConfig


urlpatterns = [
    path('blog/', RecordListView.as_view(), name='record_list'),
    path('blog/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('blog/create', RecordCreateView.as_view(), name='record_create'),
]
