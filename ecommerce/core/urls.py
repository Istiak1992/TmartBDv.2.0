from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', ProductAV.as_view(), name="ProductAV"),
    path('cat/', CategorytAV.as_view(), name="CategorytAV"),
    path('banner/', BannerAV.as_view(), name="BannerAV"),
    path('productDetails/<int:pk>/', ProductDetailsAV.as_view(), name="productDetails"),
    path('order/', OrderAV.as_view(), name="order"),
    path('shipping/', ShippingAV.as_view(), name="shipping"),
    path('search/', SearchAPIView.as_view())
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)