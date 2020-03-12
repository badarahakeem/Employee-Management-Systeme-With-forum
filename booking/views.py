from django.shortcuts import render,redirect
from django.forms.fields import DateTimeField
from .forms import BookingForm
from .models import Booking
from django.contrib import messages

# Create your views here.


# @login_required(login_url="/login/")
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            user = request.user
            instance.user = user
            instance.save()
            # form.save()
            messages.success(request,'Leave the request sent, wait for the response from the HRD',extra_tags = 'alert alert-success alert-dismissible show')
            return redirect('book')
    else:
        form = BookingForm()
    return render(request,'book.html',{"form":form})