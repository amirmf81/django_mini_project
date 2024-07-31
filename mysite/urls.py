"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views.register_view import register_view_func
from myapp.views.admin_view.get_flughts_information_view import get_flights_information_view_func
from myapp.views.create_airline import create_airline_view_func
from myapp.views.admin_view.get_passengers_view import get_passengers_view_func
from myapp.views.search_flights_view import search_flight_view_func

urlpatterns = [
#    path('admin/', admin.site.urls),
    path('register/', register_view_func),
    path('admin/get_flight_information/', get_flights_information_view_func),
    path('create_airline/', create_airline_view_func),
    path('admin/get_passengers/', get_passengers_view_func),
    path('search_flights/', search_flight_view_func),
]