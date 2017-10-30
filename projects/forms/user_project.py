from django import forms
from projects.models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description', 'project_file']
        #labels = {'resident_id' : 'Residential No/Passport No'}