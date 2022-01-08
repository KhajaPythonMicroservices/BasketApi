from django.db import models


class CustomerBasket(models.Model):
    """
    This represents the Customer Basket
    """

    class Meta:
        db_table = "customer_basket"

    buyer_id = models.IntegerField()


class BasketItem(models.Model):
    """
    This represents the BasketItem Model
    """

    class Meta:
        db_table = 'basket_items'

    product_id = models.IntegerField()
    product_name = models.CharField(max_length=256)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    discount_amount = models.FloatField()
    effective_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_basket = models.ForeignKey(to=CustomerBasket, on_delete=models.CASCADE)
