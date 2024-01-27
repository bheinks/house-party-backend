from rest_framework import viewsets
from .models import Drink, Patron, Order, OrderItem, Sound
from .serializers import DrinkSerializer, PatronSerializer, OrderSerializer, OrderItemSerializer, SoundSerializer


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class PatronViewSet(viewsets.ModelViewSet):
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
