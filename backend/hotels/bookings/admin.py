from django.contrib import admin
from .models import Hotel, Booking, Room, RoomCategory


admin.site.register(Hotel)
admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Booking)
