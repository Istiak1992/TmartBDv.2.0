from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.filters import SearchFilter

# Create your views here.

class ProductAV(APIView):
    
    def get(self, request):
        DS = Product.objects.all()
        serializer = ProductSerializer(DS, many=True)
        return Response(serializer.data)


class ProductDetailsAV(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
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



class OrderAV(APIView):
    # return a list of data
    def get(self, request):
        DS = Order.objects.all()
        serializer = OrderSerializer(DS, many=True)
        return Response(serializer.data)
    
    # Data insertion through the POST API
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShippingAV(APIView):
    # return a list of data
    def get(self, request):
        DS = Shipping.objects.all()
        serializer = ShippingSerializer(DS, many=True)
        return Response(serializer.data)
    
    # Data insertion through the POST API
    def post(self, request, format=None):
        serializer = ShippingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SearchAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['product_name']