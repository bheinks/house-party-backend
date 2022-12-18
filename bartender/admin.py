import nested_admin

from django.contrib import admin
from .models import Drink, Patron, Order, OrderItem


class DrinkAdmin(admin.ModelAdmin):
    list_display = 'name', 'price_usd'


class OrderItemInline(nested_admin.NestedTabularInline):
    model = OrderItem
    readonly_fields = 'total_usd',
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = 'created', 'total_usd', 'patron', 'settled'
    readonly_fields = 'total_usd',
    inlines = [OrderItemInline]


class OrderInline(nested_admin.NestedTabularInline):
    model = Order
    extra = 0
    readonly_fields = 'total_usd',
    inlines = [OrderItemInline]


class PatronAdmin(nested_admin.NestedModelAdmin):
    list_display = 'name', 'balance_usd'
    readonly_fields = 'balance_usd',
    inlines = [OrderInline]


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Order, OrderAdmin)
