from django.db import models
from carts.models import Cart
from django.db.models.signals import pre_save,post_save
from ecommerce.utils  import unique_order_id_generator

import math

# Create your models here.


ORDER_STATUS_CHOICES=(
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)
#order_id 
class Order(models.Model):
    

    ''' set of random string'''
    order_id            =models.CharField(max_length=120,blank=True)
    # billing_profile     =

    # shipping_address    =
    # billing_address     =
    cart                =models.ForeignKey(Cart,on_delete=models.CASCADE)
    status              =models.CharField(max_length=120,default='created')
    shipping_total      = models.DecimalField(default=5.00, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)



    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total=self.cart.total
        shipping_total=self.shipping_total
        new_total = math.fsum([cart_total, shipping_total])
        formatted_total = format(new_total, '.2f')
        self.total = formatted_total
        self.save()
        return new_total

def pre_save_create_order_id(sender, instance, *args, **kwargs):
    print("preorder")
    if not instance.order_id:
        print("inside if preorder")
        instance.order_id = unique_order_id_generator(instance)


def post_save_cart_total(sender, instance,created, *args, **kwargs):
    print("beforeifpostcart")
    if not created:
        print("postcart")
        cart_obj=instance
        cart_total=cart_obj.total
        cart_id=cart_obj.id
        qs=Order.objects.filter(cart__id=cart_id)
        if qs.count()==1 :
            order_obj=qs.first()
            order_obj.update_total()


    
pre_save.connect(pre_save_create_order_id, sender=Order)
post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    print("running")
    if created:
        print("Updating... first")
        instance.update_total()


post_save.connect(post_save_order, sender=Order)

