from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.contrib import admin

urlpatterns = [   
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    # path('cars/<name>/', find_cars_by_name, name='cars_name'),
    path('car/<id>/', find_by_id, name='car_id'),
    path('update/<id>/', update_car, name='update_car'),
    path('delete/<id>/', delete_car, name='delete_car'),
    path('search/', search, name='search'),
    path('users/', users, name='users'),
    path('addcar/', addcar, name='addcar'),
    path('adduser/', add_user, name='adduser'),
    path('updateuser/<id>/', update_user, name='update_user'),
    path('deleteuser/<id>/', delete_user, name='delete_user'),
    path('user/<id>/', find_user_by_id, name='user_id'),
    path('reservation/', reserve_car, name='reservation'),
    path('reservations/', reservations, name='reservations'),
    path('reservation/<id>/', find_reservation_by_id, name='reservation_id'),
    path('searchreservation/',search_reservations, name='searchreservations'),
    path('deletereservation/<id>/', delete_reservation, name='delete_reservation'),
    path('updatereservation/<id>/', update_reservation, name='update_reservation'),
    path('searchuser/', research_user, name='search_user'),
    path('logout/', logout_view, name='logout'),
    path('register_user/', register_user, name='register_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

