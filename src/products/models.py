from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(max_digits=100, decimal_places=2,default=39.9)
    image=models.FileField(upload_to='products/',null=True,blank=True)

    def __str__(self):
        return self.title
