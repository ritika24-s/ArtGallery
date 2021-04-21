from django.db import models
from djmoney.models.fields import MoneyField
from users.models import Users

# Create your models here.
class Products(models.Model):
    slug = models.SlugField(max_length=30,
                            unique=True,
                            help_text='A label for URL')
    description = models.TextField(help_text='description')
    cost = MoneyField(decimal_places=2, max_digits=8,
                            default_currency = 'INR')
    title = models.TextField(max_length=50, help_text='Title')
    units_left = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_total = models.MoneyField(decimal_places=2, max_digits=8,
                                    amount_default=250, currency_default='INR')
    order_date = models.DateField('date ordered', auto_now=True)

    def __str__(self):
        return "{} bought {} on {}".format(self.user.name, self.product.title, self.order_date.strftime('%Y-%m-%d'))

    class Meta:
        get_latest_by = 'order_date'
        ordering = [-'order_date']