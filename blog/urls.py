from django.urls import path

from blog.apps import BlogConfig
from blog.views import RecordDetailView, RecordListView


app_name = BlogConfig


urlpatterns = [
    path('blog/', RecordListView.as_view(), name='record_list'),
    path('blog/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
]
