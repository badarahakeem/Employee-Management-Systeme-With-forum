from django.db import models
from django.utils.translation import ugettext as _
# from django.contrib.auth.models import User
from access.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.
SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'

LEAVE_TYPE = (
(SICK,'Sick Leave'),
(CASUAL,'Casual Leave'),
(EMERGENCY,'Emergency Leave'),
(STUDY,'Study Leave'),
)



class Leave(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,)
	title = models.CharField(max_length=50, verbose_name=_('Object'),null=False, blank=True)
	startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
	reason = models.TextField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)


	# hrcomments = models.ForeignKey('CommentLeave') #hide

	status = models.CharField(max_length=12, default='pending') #pending,approved,rejected,cancelled
	is_approved = models.BooleanField(default=False) #hide
	is_cancelled = models.BooleanField(default=False) #hide

	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateField(auto_now=False, auto_now_add=True)



	class Meta:
		verbose_name = _('Leave')
		verbose_name_plural = _('Leaves')
		ordering = ['-created'] #recent objects



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype, self.user))

