from django.urls import path

from . import views

urlpatterns = [
    # as_view() not required below because configured in views.py
    path('', views.product_list_create_view, name='product-list'),
    # path('', views.product_mixin_view),
    # The / 'slash at the end is important
    path(
        '<int:pk>/',
        views.ProductDetailAPIView.as_view(),
        name='product-detail',
    ),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_delete_view),
]
