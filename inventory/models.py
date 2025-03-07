from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="")
    item_code = models.CharField(max_length=25, null=False, blank=False, default="")
    publisher = models.CharField(max_length=100, null=False, blank=False, default="")
    location = models.CharField(max_length=100, null=False, blank=False, default="")
    cost = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False, default=0)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True) 
    #whenever save record, will be updated with current date

    def __str__(self) -> str:
        return self.name 

    

