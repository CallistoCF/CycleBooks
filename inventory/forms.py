from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'item_code', 'publisher', 'location', 'cost', 'quantity_in_stock', 'quantity_sold']

class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'item_code', 'publisher', 'location', 'cost', 'quantity_in_stock', 'quantity_sold']
