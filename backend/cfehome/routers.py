from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('product',ProductViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
