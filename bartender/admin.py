import nested_admin

from django.contrib import admin
from .models import Drink, Patron, Order, OrderItem


class DrinkAdmin(admin.ModelAdmin):
    list_display = 'name', 'price_usd', 'in_stock'
    list_editable = 'in_stock'


class OrderItemInline(nested_admin.NestedTabularInline):
    model = OrderItem
    readonly_fields = 'total_usd',
    extra = 0


class OrderAdmin(nested_admin.NestedModelAdmin):
    list_display = 'created', 'total_usd', 'patron', 'settled'
    list_editable = 'settled',
    list_filter = 'settled', 'patron__name'
    readonly_fields = 'total_usd',
    inlines = [OrderItemInline]


class OrderInline(nested_admin.NestedTabularInline):
    model = Order
    readonly_fields = 'total_usd',
    extra = 0
    inlines = [OrderItemInline]


class PatronAdmin(nested_admin.NestedModelAdmin):
    list_display = 'name', 'balance_usd'
    
    readonly_fields = 'balance_usd',
    inlines = [OrderInline]


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Patron, PatronAdmin)
admin.site.register(Order, OrderAdmin)
