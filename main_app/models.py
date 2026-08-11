from django.db import models


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    # item_image = models.CharField(max_length=500, default='https://cdn-icons-png.flaticon.com/512/1377/1377194.png')
    item_image = models.ImageField(upload_to='items/', blank=True, null=True)
