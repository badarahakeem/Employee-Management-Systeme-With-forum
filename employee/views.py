from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Employee,Response
from access.models import User
from leave.models import Leave
from leave.forms import LeavehrdForm
from booking.models import Booking
from chat.models import Post
from chat.forms import PostForm, CommentForm
from . forms import EmployeeCreateForm,ResponseForm,UserForm
from django.contrib.auth.decorators import login_required




@login_required(login_url="/login/")
def hrd_index(request):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	emp = Employee.objects.all()
	leave = Leave.objects.all()
	booking = Booking.objects.all()
	user = User.objects.all()
	# on_user = request.user
	# employee =on_user.employee
	template = "index.html"
	context={
		"emp":emp,
		"booking":booking,
		"leave":leave,
		"user":user,
		# "employee":employee
	}

	return render(request, template, context)


# --------------fonction CRUD pour la gestion des employees  --------------->

@login_required(login_url="/login/")
def hrd_emp_details(request, id):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	empid = get_object_or_404(Employee, id=id)
	# delt = get_object_or_404(Employee, id=id)
	if request.method == "POST":
		empid.delete()
		messages.success(request,'Account Deleted Successfully !!!',extra_tags = 'alert alert-success alert-dismissible show')
		return redirect("hrdindex")
	template = "hrd_emp_details.html"
	context = {
		'empid':empid,
		# 'delt':delt,
		}
	return render(request, template, context)


@login_required(login_url="/login/")
def hrd_emp_create(request):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	form = EmployeeCreateForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return  redirect('hrdindex')
		else:
			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('emp_create')

	template = 'hrd_employee_create.html'
	context = {
		'form':form,
	}
	return render(request, template ,context)


@login_required(login_url="/login/")
def hrd_emp_edit(request, id):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	instance = get_object_or_404(Employee, id=id)
	form = EmployeeCreateForm(request.POST or None,instance = instance)
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request,'Account Updated Successfully !!!',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect("hrdindex")
		else:
			messages.error(request,'Error Updating account',extra_tags = 'alert alert-warning alert-dismissible show')
			return HttpResponse("Form data not valid")
	template = "hrd_emp_edit.html"
	context = {
		'instance':instance,
		'form':form,
	}
	return render(request, template,context)



# --------------fonction CRUD pour la gestion de congee   --------------->
@login_required(login_url="/login/")
def hrd_leave_all(request):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	leave_all = Leave.objects.all()
	template = "hrd_leave_all.html"
	context = {"leave_all":leave_all}
	return render(request, template, context)


@login_required(login_url="/login/")
def hrd_leave_details(request, id):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	leaveid = get_object_or_404(Leave, id=id)
	if request.method == "POST":
		leaveid.delete()
		messages.success(request,'Leave Deleted Successfully !!!',extra_tags = 'alert alert-success alert-dismissible show')
		return redirect("hrdindex")
	template = "hrd_leave_details.html"
	context = {
		'leaveid':leaveid,
		}
	return render(request, template, context)


@login_required(login_url="/login/")
def hrd_leave_status(request, id):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect("/login/")
	instance = get_object_or_404(Leave, id=id)
	form = LeavehrdForm(request.POST or None, instance=instance)
	if request.method=="POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return redirect("leave_all")
		else:
			pass
	template = "hrd_leave_status.html"
	context = {
		"instance":instance, 
		"form":form,
		}
	return render(request, template, context)

# def hrd_status_all(request):
# 	response = Response.objects.all()
# 	template = "hrd_status_all.html"
# 	context = {
# 		"response":response,
# 	}
# 	return render(request, template, context)


@login_required(login_url="/login/")
def hrd_response_create(request):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	form = ResponseForm(request.POST or None)
	response = Response.objects.all()
	leave = Leave.objects.all()
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return  redirect('response_all')
		else:
			messages.error(request,'Trying to create dublicate employees with a single user account ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('employeecreate')

	template = 'hrd_response_create.html'
	context = {
		'form':form,
		"response":response,
		'leave':leave,
	}
	return render(request, template ,context)


@login_required(login_url="/login/")
def hrd_response_details(request, id):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	responseid = get_object_or_404(Response, id=id)
	template = "hrd_response_details.html"
	context = {
		"responseid":responseid,
	}
	return render(request, template, context)


# <----------------------------forum-------------------------->

@login_required(login_url="/login/")
def hrd_postviews(request):
    chat = Post.objects.all().order_by('-created_on')
    paginator = Paginator(chat, 2) #show 10 employee lists per page

    page = request.GET.get('page')
    chat = paginator.get_page(page)
    if request.method == 'POST':
        posted = PostForm(request.POST)
        if posted.is_valid():
            instance = posted.save(commit=False)
            user = request.user
            instance.user = user
            instance.save()
            messages.success(request,'publication successfully sent',extra_tags = 'alert alert-success alert-dismissible show')
            return redirect('postcreate')
        messages.error(request,'failed to send publication',extra_tags = 'alert alert-warning alert-dismissible show')
    else:
        posted = PostForm()
    return render(request, "hrd_post_views.html" ,{'chat':chat,'posted':posted})


@login_required(login_url="/login/")
def hrd_postdetail(request, id):
    obj = get_object_or_404(Post, id=id)
    com = obj.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #datas = form.cleaned_data
            #content = datas["body"]
            new_comment = comment_form.save(commit=False)
            
            new_comment.post = obj
            user = request.user
            new_comment.user = user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "hrd_post_detail.html",{'obj':obj,'com':com,'comment_form':comment_form})


# <---------------user------------------->
@login_required(login_url="/login/")
def hrd_user(request):
	if not (request.user.is_authenticated and request.user.is_admin and request.user.is_staff):
		return redirect('/login/')
	user = User.objects.all()
	form = UserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			messages.success(request,'User added successfully',extra_tags = 'alert alert-success alert-dismissible show')
			return  redirect('hrd_user')
		else:
			messages.error(request,'Please check your credentials, Sorry no registration!! :-) ',extra_tags = 'alert alert-warning alert-dismissible show')
			return redirect('hrd_user')
	template = "hrd_user.html"
	context={

		"user":user,
		"form":form,
	}

	return render(request, template, context)

