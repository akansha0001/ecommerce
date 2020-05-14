from django.db import models
from carts.models import Cart
from django.db.models.signals import pre_save
from ecommerce.utils  import unique_order_id_generator

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



def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Order)