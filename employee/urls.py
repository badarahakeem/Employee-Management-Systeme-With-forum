from django.urls import path
from . import views


urlpatterns = [
	path('hrd_index/', views.hrd_index, name='hrdindex'),
	path('user/', views.hrd_user, name='hrd_user'),
	path('employee/create/', views.hrd_emp_create, name='emp_create'),
	path('employee/details/<int:id>/', views.hrd_emp_details, name='hrd_emp_details'),
	path('employee/edit/<int:id>/', views.hrd_emp_edit, name='emp_edit'),
	path('leave/all/', views.hrd_leave_all, name='leave_all'),
	path('leave/details/<int:id>/', views.hrd_leave_details, name='hrd_leave_details'),
	path('leave/status/<int:id>/', views.hrd_leave_status, name='leave_status'),
	path('leave/response/all/', views.hrd_response_create, name='response_all'),
	path('leave/response/details/<int:id>/', views.hrd_response_details, name='details_response'),
	path("post/views/", views.hrd_postviews, name="hrd_post"),
    path("post/details/<int:id>/", views.hrd_postdetail, name="hrd_post_detail"),
]