from rest_framework import serializers
from . import models


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=100, default="SMALL")
    order_status = serializers.HiddenField(default="PENDING")
    quantity = serializers.IntegerField()

    class Meta:
        model = models.Order
        fields = ['size', 'order_status', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    # size = serializers.CharField(max_length=100, default="SMALL")
    # order_status = serializers.HiddenField(default="PENDING")
    # quantity = serializers.IntegerField()

    class Meta:
        model = models.Order
        fields = ['size', 'order_status',
                  'quantity', 'create_at', 'update_at']


class UpdateOrderstatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['order_status']


class GetUserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['size', 'order_status', 'quantity', 'customer']
