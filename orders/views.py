from django.shortcuts import render
from yaml import serialize
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import get_object_or_404
# Create your views here.
from drf_yasg.utils import swagger_auto_schema


class HelloOrder(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "hello orders"}, status=status.HTTP_200_OK)


class OrderCreateListView(generics.GenericAPIView):
    '''
    set serializer class and queryset

    '''
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Get List all orders")
    def get(self, request):
        '''
        get all orders form order model
        serialize query data  and return response
        '''

        order = Order.objects.all()
        serializer = self.serializer_class(instance=order, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="Create order")
    def post(self, request):
        '''
        get posted data validate over serializer save and return data
        else throw error
        '''
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    serializer_class = serializers.OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]


    @swagger_auto_schema(operation_summary="Get order by id")
    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        if serializer.is_valid:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="update  order by id")
    def put(self, request, order_id):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="delete order by id")
    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.UpdateOrderstatusSerializer
    # queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(operation_summary="update order status by id")
    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        serializer = self.serializer_class(data=data, instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserOrderView(generics.GenericAPIView):
    serializer_class = serializers.GetUserOrderSerializer
    queryset = Order.objects.all()

    @swagger_auto_schema(operation_summary="Get List all orders for a spacific user")
    def get(self, request, user_id):
        order = Order.objects.filter(customer=user_id)
        serializer = self.serializer_class(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GetUserDetailOrderView(generics.GenericAPIView):
    serializer_class = serializers.GetUserOrderSerializer
    queryset = Order.objects.all()

    @swagger_auto_schema(operation_summary="Get user order by order id")
    def get(self, request, user_id, order_id):
        order = Order.objects.filter(customer=user_id)
        order_detail = get_object_or_404(order, pk=order_id)
        serializer = self.serializer_class(instance=order_detail)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
