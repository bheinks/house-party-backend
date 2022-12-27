from rest_framework import serializers
from .models import Drink, Patron, Order, OrderItem


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    drink_id = serializers.PrimaryKeyRelatedField(queryset=Drink.objects.all())

    class Meta:
        model = OrderItem
        fields = 'id', 'drink_id', 'quantity', 'total'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)
    patron = serializers.SlugRelatedField(slug_field='name', queryset=Patron.objects.all(), required=False)

    class Meta:
        model = Order
        fields = 'id', 'order_items', 'total', 'patron', 'settled', 'created'
    
    # Include patron name when returning Order, exclude when returning Patron
    def __init__(self, *args, **kwargs):
        if 'context' not in kwargs:
            self.fields.pop('patron')

        super().__init__(*args, **kwargs)
    
    def update(self, instance, validated_data):
        # Update settled?
        instance.settled = validated_data.get('settled', instance.settled)
        
        # Loop over, construct and add order items to order if provided
        order_items = validated_data.pop('order_items', [])
        for o in order_items:
            #print(o)
            order_item = OrderItem(order_id=instance.id, drink=o['drink_id'], quantity=o['quantity'])
            order_item.save()
            instance.order_items.add(order_item)

        return super().update(instance, validated_data)


class PatronSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Patron
        fields = 'id', 'name', 'orders', 'balance', 'photo'
