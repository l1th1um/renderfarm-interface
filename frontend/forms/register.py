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

    '''
    email = forms.EmailField(max_length=254,
    						label='Email Address',
    						min_length=5)
    name = forms.CharField(max_length=30, min_length=3)
    address = forms.CharField(max_length=254, widget=forms.Textarea())
    phone = forms.CharField(max_length=30)
    office_phone = forms.CharField(max_length=30)
    institution = forms.CharField(max_length=150)
    job_title = forms.CharField(max_length=30)
    resident_id = forms.CharField(max_length=50, label='Residential No/Passport No')
    resident_file = forms.FileField()
    accept = forms.BooleanField(error_messages={'required' : 'Please Accept Terms and Condition Before Using Our Service'})
    '''
    '''
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )
	'''

'''
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        
        if not name and not email:
            raise forms.ValidationError('Error !')
'''