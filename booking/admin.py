from django.contrib import admin
from .models import Booking, Room
# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room','start_time','end_time','user')


admin.site.register(Room)