from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name="home"),
    path('add_rooms/', views.AddRooms, name="addRoom"),
    path('get_room/<int:room_id>/', views.GetRoom, name="getRoom"),
    path('get_all_rooms/', views.getRoomsList, name="getAllRooms")
]