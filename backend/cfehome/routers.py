from rest_framework.routers import DefaultRouter

# routers normally can go into the urls.py

from products.viewsets import ProductViewSet, ProducGenericViewSet

router = DefaultRouter()
router.register('product-abc', ProducGenericViewSet, basename='products')
# print(router.urls)
urlpatterns = router.urls
