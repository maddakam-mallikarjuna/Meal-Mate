from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('addnewrestaurent/<int:userid>/',views.addrestaurentpage, name='addnewrestaurant'),
    path('addrestaurant/<int:userid>/', views.addrestaurent, name="addrestaurent"),
    path('viewrestaurantmenu/<int:userid>/<int:restaurantid>', views.viewmenuPage, name='viewrestaurantmenu'),
    path('addmenuitemPage/<int:userid>/<int:restaurantid>', views.addMenuItemPage, name="addmenuitemPage"),
    path('addmenuitem/<int:userid>/<int:restaurantid>', views.addMenuItem, name="addmenuitem"),
    path('deleterestaurant/<int:userid>/<int:restaurantid>', views.removeRestaurant, name="deleterestaurant"),
    path('deletemenuitem/<int:userid>/<int:restaurantid>/<int:menuid>/', views.deletemenuitem, name="deletemenuitem"),
    path('editmenuitem/<int:userid>/<int:restaurantid>/<int:menuid>/', views.editmenuitemPage, name="editmenuitem"),
    path('editmenuitems/<int:userid>/<int:restaurantid>/<int:menuid>/', views.editedMenuItem, name="editmenuitems"),
]
