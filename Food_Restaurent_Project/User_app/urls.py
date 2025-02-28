from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('userHome/<int:userid>/', views.userHome, name="userHome"),
    path('openmenu/<int:userid>/<int:restid>/',views.openmenu, name='openmenu'),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path('viewmycart/<int:userid>/', views.open_cart, name="viewmycart"),
    path('remove_cart_item/<int:userid>/<int:itemid>/', views.remove_cart_item, name="remove_cart_item"),
    path('checkout/<int:userid>/', views.checkout, name="checkout"),
    path("success/<int:userid>/", views.payment_success, name="payment_success"),
]