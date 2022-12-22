from rest_framework import serializers
from .models import Drink, Patron, Order, OrderItem


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        exclude = 'id',


class OrderItemSerializer(serializers.ModelSerializer):
    drink = serializers.SlugRelatedField(slug_field='name', queryset=Drink.objects.all())

    class Meta:
        model = OrderItem
        fields = 'id', 'drink', 'quantity', 'total'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)
    patron = serializers.SlugRelatedField(slug_field='name', queryset=Patron.objects.all(), required=False)

    class Meta:
        model = Order
        fields = 'id', 'order_items', 'total', 'patron', 'settled', 'created'
    
    # Include patron name when returning Order, exclude when returning Patron
    def __init__(self, *args, **kwargs):
        if 'context' not in kwargs:
            del self.fields['patron']

        super().__init__(*args, **kwargs)
    
    def update(self, instance, validated_data):
        # Update settled?
        instance.settled = validated_data.get('settled', instance.settled)
        
        # Loop over, construct and add order items to order if provided
        order_items = validated_data.pop('order_items', [])
        for o in order_items:
            order_item = OrderItem(order_id=instance.id, **o)
            order_item.save()
            instance.order_items.add(order_item)

        return super().update(instance, validated_data)


class PatronSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Patron
        fields = 'name', 'orders', 'balance'
