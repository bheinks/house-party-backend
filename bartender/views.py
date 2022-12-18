from rest_framework import viewsets
from .models import Drink, Patron, Order, OrderItem
from .serializers import DrinkSerializer, PatronSerializer, OrderSerializer


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class PatronViewSet(viewsets.ModelViewSet):
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
