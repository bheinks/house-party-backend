from rest_framework import serializers
from .models import Drink, Patron, Order, OrderItem, Sound


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    drink = serializers.SlugRelatedField(slug_field='name', queryset=Drink.objects.all())

    class Meta:
        model = OrderItem
        fields = 'id', 'drink', 'quantity', 'total'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=False)
    patron = serializers.SlugRelatedField(slug_field='name', queryset=Patron.objects.all())

    class Meta:
        model = Order
        fields = 'id', 'order_items', 'total', 'patron', 'settled', 'created'

    def create(self, validated_data):
        order_items = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)

        for order_item in order_items:
            OrderItem.objects.create(order=order, **order_item)

        return order

    def update(self, instance, validated_data):
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
        fields = 'id', 'name', 'orders', 'balance', 'photo'


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = '__all__'
