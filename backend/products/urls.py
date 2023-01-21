from django.urls import path

from . import views

urlpatterns = [
    # The / 'slash is important
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
