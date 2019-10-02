from .models import SerialNo, Order, Status, Users
from rest_framework import serializers

class SerialNoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SerialNo
        fields = '__all__'

class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class OrderCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class StatusBooleanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'



