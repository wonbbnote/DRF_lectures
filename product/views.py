from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from product.models import Product
from datetime import datetime

from product.serializer import ProductSerializer
from django.db.models import Q


# Create your views here.
class ProductView(APIView):
    # validate
    def get(self, request):
        today = datetime.now()
        products = Product.objects.filter(
            Q(exposure_start_date__lte = today, exposure_end_date__gte = today)|
            Q(writer = request.user)
        )
        return Response(ProductSerializer(products, many=True).data)
    # create
    def post(self, request):
        user = request.user
        request.data['writer'] = user.id
        product_serializer = ProductSerializer(data=request.data)
        print(product_serializer)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({"message":"저장!"})
        return Response({"message":"저장실패!"})
    # update
    def put(self, request, id):
        product = Product.objects.get(id=id)
        user = request.user
        request.data['writer'] = user.id
        product_serializer = ProductSerializer(data=request.data, partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)
