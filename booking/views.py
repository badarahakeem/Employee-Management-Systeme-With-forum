from django.shortcuts import render,redirect
from django.forms.fields import DateTimeField
from .forms import BookingForm
from .models import Booking
from django.contrib import messages

# Create your views here.



# def confirm(request, pk = None):
#     if request.method == 'POST':
#         if pk:
#             invalid_dates = False
#             #get the room 
#             room = Room.objects.get(pk = pk)
#             user = request.user
#             start_time = request.session['start_time'] 
#             end_time = request.session['end_time']

#             # check wether the dates are valid
#             # case 1: a room is booked before the start_time date, and checks out after the requested start_time date
#             case_1 = Booking.objects.filter(room=room, start_time__lte=start_time, end_time__gte=start_time).exists()

#             # case 2: a room is booked before the requested end_time date and end_time date is after requested end_time date
#             case_2 = Booking.objects.filter(room=room, start_time__lte=end_time, end_time__gte=end_time).exists()

#             case_3 = Booking.objects.filter(room=room, start_time__gte=start_time, end_time__lte=end_time).exists()


#             # if either of these is true, abort and render the error
#             if case_1 or case_2 or case_3:
#                   return render(request, "book.html", {"errors": "This room is not available on your selected dates"})                  

#              # dates are valid             
#              booking = Booking(
#              start_time = start_time, 
#              end_time = end_time,
#              room_id = room.id,
#              user = user.id
#              )

#              booking.save()

#              #redirect to success page (need to define this as a separate view)
#              return redirect("booking_success")


#       return render(request, "book.html", args)


def booking(request):
    bk = Booking.objects.all().exclude(end_time__isnull=True)
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = request.user
            instance.user = user
            instance.save()
            # form.save()
            messages.success(request,'Your request has been sent successfully, wait for the response from the HRD',extra_tags = 'alert alert-success alert-dismissible show')
            return redirect('createleave')
        messages.error(request,'echec de demande de congé, veuillez vérifier les dates d\'entrée',extra_tags = 'alert alert-warning alert-dismissible show')
    else:
        form = BookingForm()
    return render(request,'book.html',{"form":form, 'bk':bk})