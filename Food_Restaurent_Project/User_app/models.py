from django.db import models
from Admin_app.models import Restaurents, MenuItems
from Main_app.models import Users

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_cart')
    item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.item.itemname} ({self.quantity})"

        