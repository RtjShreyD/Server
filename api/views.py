from django.shortcuts import render
from rest_framework import viewsets
from .models import SerialNo, Order, Status, Transaction
from .serializers import ( SerialNoListSerializer, 
                           StatusBooleanSerializer, 
                           OrderCreateSerializer, 
                           OrderListSerializer,
                           LoggerSerializer,
                           TransactionSerializer,
)

class SerialNoListView(viewsets.ModelViewSet):
    queryset = SerialNo.objects.all()
    serializer_class = SerialNoListSerializer

class OrderCreateStatusSetView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderListView():
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class TransactionListView():
    queryset = Transaction.objects.all()
    serializer_class = LoggerSerializer