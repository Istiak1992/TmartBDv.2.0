from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', ProductAV.as_view(), name="ProductAV"),
    path('cat/', CategorytAV.as_view(), name="CategorytAV"),
    path('banner/', BannerAV.as_view(), name="BannerAV"),
    path('productDetails/<int:pk>/', ProductDetailsAV.as_view(), name="productDetails"),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)