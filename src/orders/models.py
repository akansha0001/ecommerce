from django.db import models
from carts.models import Cart
from django.db.models.signals import pre_save,post_save
from ecommerce.utils  import unique_order_id_generator
from billing.models import BillingProfile
import math

# Create your models here.


ORDER_STATUS_CHOICES=(
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)
#order_id 

class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created = False
        qs = self.get_queryset().filter(
                billing_profile=billing_profile, 
                cart=cart_obj, 
                active=True)
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(
                    billing_profile=billing_profile, 
                    cart=cart_obj)
            created = True
        return obj, created



class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True,on_delete=models.CASCADE)
    order_id        = models.CharField(max_length=120, blank=True) # AB31DE3
    # billing_profile = ?
    # shipping_address
    # billing_address 
    cart            = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status          = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total  = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active          = models.BooleanField(default=True)

    objects = OrderManager()


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
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


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
