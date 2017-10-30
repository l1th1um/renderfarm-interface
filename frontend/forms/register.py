from django import forms
from users.models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','first_name']
        labels = {'first_name' : 'Name'}

class ProfileForm(forms.ModelForm):
    accept = forms.BooleanField(
        error_messages={'required': 'Please Accept Terms and Condition Before Using Our Service'})

    class Meta:
        model = Profile
        fields = ['address', 'phone', 'office_phone', 'institution', 'job_title', 'resident_id', 'resident_file']
        labels = {'resident_id' : 'Residential No/Passport No'}