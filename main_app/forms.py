from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        # Model Item aus den models.py wird genutzt
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
