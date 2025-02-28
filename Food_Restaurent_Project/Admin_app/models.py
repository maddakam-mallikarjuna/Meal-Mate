from django.db import models
from Main_app.models import Users

class Restaurents(models.Model):
    owner = models.ForeignKey('Main_app.Users', on_delete=models.CASCADE , related_name="restaurants")

    restaurentname = models.CharField(max_length=120)
    restaurentimage = models.TextField()
    restaurentcusines = models.TextField()
    restaurentopenig = models.TextField()
    restaurantclosing = models.TextField()
    restaurantaddress = models.TextField()

    def __str__(self):
        return f"{self.restaurentname} {self.restaurentcusines}  {self.restaurantaddress} "

    
class MenuItems(models.Model):
    restaurant = models.ForeignKey('Admin_app.Restaurents', on_delete=models.CASCADE, related_name='menu')

    itemname = models.CharField(max_length=130)
    itemdescription = models.TextField()
    itemimage = models.TextField()
    itemstyles = models.TextField()
    itemprice = models.FloatField()
    itemdiscount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.itemname} {self.restaurant} {self.itemdescription} ${self.itemprice}"