from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        exclude = ['user', 'is_validated']

    def clean(self):
        """
        Check global form constraints
        """
        cleaned_data = super().clean()
        is_validated = cleaned_data.get('is_validated')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # When validating, check that there is no reservation at that time
        if is_validated:
            booking_list = cleaned_data['room'].booking_set.filter(
                is_validated=True,
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exclude(pk=self.instance.pk)

            if booking_list.exists():
                raise forms.ValidationError("There is already a booking at this time.")

        # Check that end time is after start time
        if start_time and end_time and start_time > end_time:
            raise forms.ValidationError("booking must end after it begins.")

        # Check that start time is not in the past
        now = timezone.now()
        if start_time and now > start_time:
            raise forms.ValidationError("You can't make a booking in the past.")

        return cleaned_data
