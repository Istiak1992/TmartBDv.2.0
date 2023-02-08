from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin



class CartAV(APIView):
    # return a list of data
    def get(self, request):
        DS = Cart.objects.all()
        serializer = CartSerializer(DS, many=True)
        return Response(serializer.data)
    
    # Data insertion through the POST API
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class CartDetailsAV(APIView):

    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CartSerializer(snippet)
        return Response(serializer.data)

class CartViewSet(CreateModelMixin,RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    
    def get_queryset(self):
        return CartItems.objects.filter(cart_id=self.kwargs["cart_pk"])
    
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}