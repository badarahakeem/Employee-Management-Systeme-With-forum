from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from employee.models import *
from .forms import (UserLogin)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView



# def changepassword(request):
# 	if not request.user.is_authenticated:
# 		return redirect('/')
# 	'''
# 	Please work on me -> success & error messages & style templates
# 	'''
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(request.user, request.POST)
# 		if form.is_valid():
# 			user = form.save(commit=True)
# 			update_session_auth_hash(request,user)

# 			messages.success(request,'Password changed successfully',extra_tags = 'alert alert-success alert-dismissible show' )
# 			return redirect('accounts:changepassword')
# 		else:
# 			messages.error(request,'Error,changing password',extra_tags = 'alert alert-warning alert-dismissible show' )
# 			return redirect('accounts:changepassword')
			
# 	form = PasswordChangeForm(request.user)
# 	return render(request,'accounts/change_password_form.html',{'form':form})




# def register_user_view(request):
# 	# WORK ON (MESSAGES AND UI) & extend with email field
# 	if request.method == 'POST':
# 		form = UserAddForm(data = request.POST)
# 		if form.is_valid():
# 			instance = form.save(commit = False)
# 			instance.save()
# 			username = form.cleaned_data.get("username")

# 			messages.success(request,'Account created for {0} !!!'.format(username),extra_tags = 'alert alert-success alert-dismissible show' )
# 			return redirect('accounts:register')
# 		else:
# 			messages.error(request,'Username or password is invalid',extra_tags = 'alert alert-warning alert-dismissible show')
# 			return redirect('accounts:register')


# 	form = UserAddForm()
# 	dataset = dict()
# 	dataset['form'] = form
# 	dataset['title'] = 'register users'
# 	return render(request,'accounts/register.html',dataset)




def login_view(request):
	'''
	work on me - needs messages and redirects
	
	'''
	form = UserLogin(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None :
			login(request, user)
			return redirect('post')
		else:
			messages.error(request,'Account is invalid',extra_tags = 'alert alert-error alert-dismissible show' )
			return redirect('login')
	return render(request,'login.html',{'form':form})



@login_required(login_url="/login/")
def user_profile_view(request):
	'''
	user profile view -> staffs (No edit) only admin/HR can edit.
	'''
	user = request.user
	employee =user.employee
	return render(request,'userprofile.html',{'employee': employee})
	# return HttpResponse("Sorry , not authenticated for this,admin or whoever you are :)")





class HomePageView(ListView):
    model = User



class UserProfileView(View):
    def get(self, request, user_id):

        try:
            user = User.objects.get(id=user_id)
        except:
            user = None

        context = {
            "viewed_user": user
        }

        return render(request, "user_profile.html", context)