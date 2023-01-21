from django.urls import path

from . import views

urlpatterns = [
    # as_view() not required below because configured in views.py
    path('', views.product_create_view),
    # The / 'slash at the end is important
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
