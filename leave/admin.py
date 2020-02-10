from django.contrib import admin
from .models import Leave
# from .models import Comment


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user','title','startdate','enddate','created','leavetype','is_approved')



