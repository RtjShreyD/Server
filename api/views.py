from django.shortcuts import render
from rest_framework import viewsets
from .models import SerialNo, Order, Status, Users 
from .serializers import ( SerialNoListSerializer, 
                           StatusBooleanSerializer, 
                           OrderCreateSerializer, 
                           UsersListSerializer,
)

class SerialNoListView(viewsets.ModelViewSet):
    queryset = SerialNo.objects.all()
    serializer_class = SerialNoListSerializer

class UsersListView(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersListSerializer

class OrderCreateView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class StatusView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusBooleanSerializer