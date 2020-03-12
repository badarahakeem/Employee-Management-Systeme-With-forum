from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',views.login_view,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # path('create-user/',views.register_user_view,name='register'),
    # path('user/change-password/',views.changepassword,name='changepassword'),
    path('user/profile/view/',views.user_profile_view, name='userprofile'),
    path('users/<user_id>/', views.UserProfileView.as_view(),name='user_profile',),
]