from django.db import models
from access.models import User
from datetime import datetime
from django.core.checks import register

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name=('comment'),
        help_text=('Describe what is special about this room, '
                    'such as available equipment.'),
    )

    def __str__(self):
        return self.name
    



class Booking(models.Model):
    
    room = models.ForeignKey(Room, verbose_name=("Meeting room"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    about = models.TextField(
            max_length=150,
            help_text=('See for example the meeting agenda.'),null=True, blank=True)
    is_validated = models.BooleanField(null=False,default=False) #hide

    class Meta:
        verbose_name = ("booking")
        verbose_name_plural = ("bookings")

    
    # def __str__(self):
    #     return str(self.start_time.hour) +"h"+ " a " + str(
    #         self.end_time.hour) +"h"+ " : " + self.room.name





    

