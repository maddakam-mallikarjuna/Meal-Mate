from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Main_app.models import Users
from .models import Restaurents, MenuItems
from django.shortcuts import get_object_or_404


def addrestaurentpage(request, userid):
    return render(request, 'Admin_app/AddRestaurants.html', {'userid':userid})

def removeRestaurant(request, userid, restaurantid):
    user = Users.objects.get(id=userid)
    rest_to_remove = Restaurents.objects.get(id=restaurantid)
    rest_to_remove.delete()
    restaurants = Restaurents.objects.filter(owner=user.id)  
    context = {'user': user}
    if restaurants.exists():
        context['restaurants'] = restaurants
    
    return render(request, 'Admin_app/AdminHomePage.html', context)
    
def addrestaurent(request, userid):
    user = get_object_or_404(Users, id=userid)
    if request.method == 'POST':
        restaurantname = request.POST.get('restaurantname')
        restaurantimage = request.POST.get('restaurantimage')
        restaurantcusine = request.POST.get('restaurantcusine')
        restaurantopening = request.POST.get('restauranttiming-open')
        restaurantclosing = request.POST.get('restauranttiming-close')
        restaurantaddress = request.POST.get('restaurantaddress')

        restaurant = Restaurents( owner=user, restaurentname=restaurantname, restaurentimage=restaurantimage, restaurentcusines=restaurantcusine, restaurentopenig=restaurantopening, restaurantclosing=restaurantclosing, restaurantaddress=restaurantaddress)
        restaurant.save()
        restaurants = Restaurents.objects.filter(owner=user.id)  
        context = { 'restaurants': restaurants, 'user': user }

        return render(request, 'Admin_app/AdminHomePage.html', context)
    
def viewmenuPage(request, userid, restaurantid):
    restaurant = Restaurents.objects.filter(id=restaurantid)
    user = Users.objects.get(id=userid)
    Menu = MenuItems.objects.filter(restaurant=restaurantid)
    if Menu.exists():
        return render(request, 'Admin_app/ViewMenuPage.html', {'menus': Menu, 'user': user, 'restaurantid': restaurantid})

    return render(request, 'Admin_app/ViewMenuPage.html', {'user': user, 'restaurantid': restaurantid})

def addMenuItemPage(request, userid,  restaurantid):
    return render(request, 'Admin_app/addMenuItemPage.html', {'restaurantid': restaurantid, 'userid': userid})

def addMenuItem(request, userid, restaurantid):
    user = Users.objects.get(id=userid)
    restaurant = Restaurents.objects.get(id=restaurantid)
    if request.method == "POST":
        itemname = request.POST.get("itemname")
        itemdescription = request.POST.get("itemdescription")
        itemimage = request.POST.get("itemimage")
        itemcusine = request.POST.get("itemcusine")
        itemprice = request.POST.get("itemprice")
        itemdiscount = request.POST.get("itemdiscount")

        item = MenuItems(restaurant=restaurant, itemname=itemname, itemdescription=itemdescription, itemimage=itemimage, itemstyles=itemcusine, itemprice=itemprice, itemdiscount=itemdiscount)
        item.save()

        Menu = MenuItems.objects.filter(restaurant=restaurantid)
        return redirect("viewrestaurantmenu", userid=userid, restaurantid=restaurantid)

def deletemenuitem(request, userid, restaurantid, menuid):
    item = MenuItems.objects.get(id=menuid)
    item.delete()

    restaurant = Restaurents.objects.filter(id=restaurantid)
    user = Users.objects.get(id=userid)
    Menu = MenuItems.objects.filter(restaurant=restaurantid)
    if Menu.exists():
        return render(request, 'Admin_app/ViewMenuPage.html', {'menus': Menu, 'user': user, 'restaurantid': restaurantid})

    return render(request, 'Admin_app/ViewMenuPage.html', {'user': user, 'restaurantid': restaurantid})

def editmenuitemPage(request, userid, restaurantid, menuid):
    item = MenuItems.objects.get(id=menuid)
    restaurant = Restaurents.objects.filter(id=restaurantid)
    user = Users.objects.get(id=userid)
    Menu = MenuItems.objects.filter(restaurant=restaurantid)
    return render(request, 'Admin_app/EditMenuItemPage.html', {'menus': Menu, 'user': user, 'restaurantid': restaurantid, 'item': item, 'userid': userid})

def editedMenuItem(request, userid, restaurantid, menuid):
    item = MenuItems.objects.get(id=menuid)

    if request.method == "POST":
        item.itemname = request.POST.get('itemname')
        item.itemdescription = request.POST.get('itemdescription')
        item.itemimage = request.POST.get('itemimage')
        item.itemstyles = request.POST.get('itemcusine')
        item.itemprice = request.POST.get('itemprice')
        item.itemdiscount = request.POST.get('itemdiscount')

        item.save()
        user = Users.objects.get(id=userid)
        restaurant = Restaurents.objects.filter(id=restaurantid)
        Menu = MenuItems.objects.filter(restaurant=restaurantid)

        # return redirect('viewrestaurantmenu', {'menus': Menu, 'user': user, 'restaurantid': restaurantid})
        return redirect("viewrestaurantmenu", userid=userid, restaurantid=restaurantid)