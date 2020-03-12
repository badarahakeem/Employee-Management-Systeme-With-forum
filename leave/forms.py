from django import forms
from .models import Leave
# from .models import Comment
import datetime

class LeaveCreationForm(forms.ModelForm):
	class Meta:
		model = Leave
		exclude = ['user','status','is_approved','is_cancelled','updated','created']



	def clean_enddate(self):
		enddate = self.cleaned_data.get('enddate')
		startdate = self.cleaned_data.get('startdate')
		today_date = datetime.date.today()

		if (startdate or enddate) < today_date:# both dates must not be in the past
			raise forms.ValidationError("both dates must not be in the past")


		elif startdate >= enddate:# TRUE -> FUTURE DATE > PAST DATE,FALSE other wise
			raise forms.ValidationError("Selected dates are wrong")

		return enddate


class LeavehrdForm(forms.ModelForm):
	class Meta:
		model = Leave
		fields = '__all__'


		