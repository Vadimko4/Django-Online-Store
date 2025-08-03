from django.urls import path

from catalog.apps import CatalogConfig
from catalog.models import Category
from catalog.views import ContactsView, ProductDetailView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryDetailView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/<int:pk>/', cache_page(60)(CategoryDetailView.as_view()), name='category_detail'),
]
