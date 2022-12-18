from rest_framework import serializers
from .models import Drink, Patron, Order, OrderItem


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        exclude = 'id',


class OrderItemSerializer(serializers.ModelSerializer):
    drink = DrinkSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = 'drink', 'quantity', 'total'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    patron = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = 'order_items', 'total', 'patron', 'settled', 'created'
    
    # Include patron name when returning Order, exclude when returning Patron
    def __init__(self, *args, **kwargs):
        if 'context' not in kwargs:
            del self.fields['patron']

        super().__init__(*args, **kwargs)


class PatronSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Patron
        fields = 'name', 'orders', 'balance'