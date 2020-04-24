from django.db import models
from datetime import datetime

class Hotel(models.Model):
    name = models.CharField(max_length=32)

class RoomCategory(models.Model):
    name = models.CharField(max_length=32)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    min_price = models.IntegerField()

class Room(models.Model):
    name = models.CharField(max_length=32)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_check_in = models.DateTimeField(default=datetime.now())
    date_check_out = models.DateTimeField(null=True)
