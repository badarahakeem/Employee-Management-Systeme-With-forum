from django import forms
from employee.models import Fliale,Employee,Response
from access.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
	# image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	class Meta:
		model = Employee
		# exclude = ['is_blocked','is_deleted','token','created','updated']
		fields = '__all__'





class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		exclude = ['update, created']


class UserForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
	    model = User
	    fields = ('email','password1','password2', 'role', 'bio')

	def clean_password2(self):
	    # Check that the two password entries match
	    password1 = self.cleaned_data.get("password1")
	    password2 = self.cleaned_data.get("password2")
	    if password1 and password2 and password1 != password2:
	        raise forms.ValidationError("Passwords don't match")
	    return password2

	def save(self, commit=True):
	    # Save the provided password in hashed format
	    user = super().save(commit=False)
	    user.set_password(self.cleaned_data["password1"])
	    if commit:
	        user.save()
	    return user