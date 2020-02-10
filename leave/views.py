from django.shortcuts import render,redirect
from .forms import LeaveCreationForm
from django.contrib import messages
from .models import Leave
from employee.models import Employee
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.




@login_required(login_url="/login/")
def leave_creation(request):
	if request.method == "POST":
		form = LeaveCreationForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			user = request.user
			instance.user = user
			instance.save()
			# form.save()
			messages.success(request,'Leave the request sent, wait for the response from the HRD',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('createleave')
		messages.error(request,'leave request failed, please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
	else:
		form = LeaveCreationForm()
	return render(request,'create_leave.html',{"form":form})
	# return HttpResponse('leave creation form')



@login_required(login_url="/login/")
def leaves_list(request):
	user = request.user
	leave = Leave.objects.filter(user=user)
	return render(request,'leavesee.html',{'leave':leave,})


@login_required(login_url="/login/")
def leaves_view(request,id):
	leave = get_object_or_404(Leave, id = id)
	# employee = Employee.objects.filter(user = leave.user)[0]
	return render(request,'leave_detail.html',{'leave':leave,})


