from django.shortcuts import render
from rest_framework import viewsets
from .models import SerialNo, Order, Status, Transaction
from .serializers import ( SerialNoListSerializer, 
                           StatusBooleanSerializer, 
                           OrderCreateSerializer, 
                           OrderListSerializer,
                           TransactionSerializer,
)

class SerialNoListView(viewsets.ModelViewSet):
    queryset = SerialNo.objects.all()
    serializer_class = SerialNoListSerializer

class OrderCreateStatusSetView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderListView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class TransactionListView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusBooleanSerializer