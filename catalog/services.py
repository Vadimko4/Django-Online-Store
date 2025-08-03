from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLE


def get_products_from_cache():
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = "dogs_list"
    products = cache.get(key)
    if products is None:
        dogs = Product.objects.all()
        cache.set(key, dogs)
    return products
