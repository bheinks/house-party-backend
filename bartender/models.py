from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator


class Drink(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='drinks', blank=True)

    def __str__(self):
        return self.name
    
    @admin.display(description='Price')
    def price_usd(self):
        return f'${self.price}'


class Patron(models.Model):
    name = models.CharField(max_length=64, unique=True)
    photo = models.ImageField(upload_to='patrons', blank=True)

    def __str__(self):
        return self.name
    
    @property
    def balance(self):
        return sum(o.total for o in self.orders.filter(settled=False))
    
    @admin.display(description='Balance')
    def balance_usd(self):
        return f'${self.balance}'


class Order(models.Model):
    drinks = models.ManyToManyField(Drink, through='OrderItem')
    settled = models.BooleanField(default=False, verbose_name='settled?')
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Placed on {self.created.strftime("%Y-%m-%d")} at {self.created.strftime("%H:%M:%S")}'

    @property
    def total(self):
        return sum(o.total for o in self.order_items.all())
    
    @admin.display(description='Total')
    def total_usd(self):
        return f'${self.total}'


class OrderItem(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        # Quick and dirty hack to conditionally pluralize drink name
        # https://stackoverflow.com/a/65063284
        return f"{self.quantity} {self.drink.name}{'s'[:self.quantity^1]}"
    
    @property
    def total(self):
        return self.drink.price * self.quantity
    
    @admin.display(description='Total')
    def total_usd(self):
        return f'${self.total}'
