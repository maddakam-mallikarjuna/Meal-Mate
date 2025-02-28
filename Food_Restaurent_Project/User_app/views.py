from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, get_object_or_404
from Admin_app.models import Restaurents, MenuItems
from Main_app.models import Users
from .models import Cart
import json
from django.http import JsonResponse
import razorpay
from Food_Restaurent_Project import settings


def userHome(request, userid):
    user = Users.objects.get(id=userid)
    restaurents = Restaurents.objects.all()
    return render(request, 'User_app/UserHomePage.html', {'restaurants': restaurents, 'userid': user.id})


def openmenu(request, userid, restid):
    restaurant = Restaurents.objects.filter(id=restid)
    menuitems = MenuItems.objects.filter(restaurant=restid)
    return render(request, 'User_app/ViewMenu.html', 
    {'restaurant': restaurant,
    'items': menuitems,
    'userid': userid,
    })

def add_to_cart(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        item_id = request.POST.get("item_id")
        quantity = int(request.POST.get("quantity"))

        if not item_id:
            return JsonResponse({"error": "Item ID is required"}, status=400)

        item = get_object_or_404(MenuItems, id=item_id)
        user = Users.objects.get(id = user_id)
        cart_item, created = Cart.objects.get_or_create(user=user, item=item)

        if created:
            cart_item.quantity = quantity  # Set quantity if new item
        else:
            cart_item.quantity += quantity  # Increase quantity if item exists

        cart_item.save()

        return JsonResponse({
            "message": "Item added to cart successfully!",
            "item_id": item.id,
            "new_quantity": cart_item.quantity
        })

    return JsonResponse({"error": "Invalid request method"}, status=405)


def open_cart(request, userid):
    user = get_object_or_404(Users, id=userid)  # Fetch user safely

    try:
        cart_items = Cart.objects.filter(user=user)  # Get user's cart items
        
        # Calculate total amount & assign final prices
        total_amount = 0
        for item in cart_items:
            discount_amount = (item.item.itemprice * item.item.itemdiscount) / 100
            item.final_price = item.item.itemprice - discount_amount 
            item.total = item.final_price * item.quantity
            total_amount += item.final_price * item.quantity  

        return render(request, 'User_app/mycartPage.html', {
            'user': user,
            'cart': cart_items,
            'total_amount': total_amount
        })
    
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)


def remove_cart_item(request, userid, itemid):
    user = get_object_or_404(Users, id=userid)  # Ensure user exists

    try:
        cart_item = Cart.objects.get(id=itemid, user=user)  # Ensure item belongs to the user
        cart_item.delete()  # Remove item from cart

        # Recalculate total amount after deleting an item
        cart_items = Cart.objects.filter(user=user)
        total_amount = 0
        for item in cart_items:
            discount_amount = (item.item.itemprice * item.item.itemdiscount) / 100
            item.final_price = item.item.itemprice - discount_amount  # Assign final price per item
            total_amount += item.final_price * item.quantity  # Sum up total amount

        return redirect('viewmycart', userid=userid)  # Redirect to refresh cart page

    except Cart.DoesNotExist:
        return JsonResponse({"error": "Item not found in cart."}, status=404)

def checkout(request, userid):
    user = get_object_or_404(Users, id=userid)
    
    cart_items = Cart.objects.filter(user=user)
    total_amount = 0
    for item in cart_items:
        discount_amount = (item.item.itemprice * item.item.itemdiscount) / 100
        item.final_price = item.item.itemprice - discount_amount
        total_amount += item.final_price * item.quantity  

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    order_data = {
        'amount': int(total_amount * 100),  # Convert to paise
        'currency': 'INR',
        'payment_capture': '1',  # Auto capture
    }

    order = client.order.create(data=order_data)

    return JsonResponse({
        "order_id": order["id"],
        "amount": order["amount"],
        "currency": order["currency"],
        "key": settings.RAZORPAY_KEY_ID,
        "user_id": user.id,
    })


def payment_success(request, userid):
    # Fetch all cart items for the user (assuming they're cleared after payment)
    cart_items = Cart.objects.filter(user_id=userid)

    # Calculate total price and discount
    cart_items_with_totals = []
    total_price = 0
    total_discount = 0

    for item in cart_items:
        item_total = item.item.itemprice * item.quantity
        item_discount = (item.item.itemprice * item.item.itemdiscount / 100) * item.quantity
        final_item_total = item_total - item_discount

        cart_items_with_totals.append({
            "item": item.item,
            "quantity": item.quantity,
            "total": final_item_total  # Store final total for each item
        })

        total_price += item_total
        total_discount += item_discount

    final_total = total_price - total_discount

    context = {
        "cart_items": cart_items_with_totals,
        "total_price": total_price,
        "total_discount": total_discount,
        "final_total": final_total
    }

    return render(request, "User_app/receipt.html", context)