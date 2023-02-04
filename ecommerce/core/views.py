from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class ProductAV(APIView):
    
    def get(self, request):
        DS = Product.objects.all()
        serializer = ProductSerializer(DS, many=True)
        return Response(serializer.data)



class CategorytAV(APIView):
    
    def get(self, request):
        DS = Category.objects.all()
        serializer = CategorySerializer(DS, many=True)
        return Response(serializer.data)


class BannerAV(APIView):
    
    def get(self, request):
        DS = Banner.objects.all()
        serializer = BannerSerializer(DS, many=True)
        return Response(serializer.data)