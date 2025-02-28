from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main_app.urls')),
    path('Admin/', include('Admin_app.urls')),
    path('', include('User_app.urls'))
]
