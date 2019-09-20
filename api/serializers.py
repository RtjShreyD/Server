from .models import SerialNo, Order, Status, Transaction
from rest_framework import serializers

class SerialNoListSerializer():
    class Meta:
        model = SerialNo
        fields = '__all__'

class OrderCreateSerializer():
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_ids = validated_data.pop('order')
        instance = Order.objects.create(**validated_data)
        for order_id in order_ids:
            instance.order_ids.add(order_ids)

        return instance

class StatusBooleanSerializer():
    class Meta:
        model = Status
        fields = '__all__'

class OrderListSerializer():
    class Meta:
        model = Order
        fields = '__all__'

class TransactionSerializer():
    class Meta:
        model = Order
        fields = '__all__'