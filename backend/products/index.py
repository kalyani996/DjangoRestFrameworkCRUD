from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'body',
        'price',
        'public',
        'path',
        'endpoint',
    ]

    tags = 'get_tags_list'