from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Admin_app.models import Restaurents

def WelcomePage(request):
    return render(request, 'Main_app/WelcomePage.html')


def Signup(request):
    return render(request, 'Main_app/SignupPage.html')

def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        mobile = request.POST.get("Mobile")
        address = request.POST.get("Address")
        userType = request.POST.get("UserType")

        try:
            temp = Users.objects.get(email = email)
            return render(request, 'Main_app/SignupPage.html', {'msg' : 'User Exits.!'})
        except  Users.DoesNotExist:
            pass

        user = Users(username=username, email=email, password=password, mobile=mobile, address=address, usertype=userType)
        user.save()

        return render(request, 'Main_app/LoginPage.html', {'msg' : False})

    return render(request, 'Main_app/SignupPage.html', {'msg' : "Enter Valid Input's"})


def Login(request):
    return render(request, 'Main_app/LoginPage.html')

def handle_login(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")

        try:
            user = Users.objects.get(email=email)
            
            if user.password == password:  
                if user.usertype == "user":
                    restaurents = Restaurents.objects.all()
                    return render(request, 'User_app/UserHomePage.html', {'restaurants': restaurents, 'userid': user.id})
                else:  
                    restaurants = Restaurents.objects.filter(owner=user.id)  

                    context = {'user': user}
                    
                    if restaurants.exists():
                        context['restaurants'] = restaurants

                    return render(request, 'Admin_app/AdminHomePage.html', context)

            else:
                return render(request, "Main_app/LoginPage.html", {'msg': 'Invalid Password'})

        except Users.DoesNotExist:
            return render(request, "Main_app/LoginPage.html", {'msg': 'No User Found.!'})

    return render(request, "Main_app/LoginPage.html")