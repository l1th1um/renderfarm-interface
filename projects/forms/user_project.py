from django import forms
from projects.models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description', 'project_file', 'main_file', 'start_frame', 'end_frame']

    def clean(self):
        form_data = self.cleaned_data
        if (form_data['start_frame'] != 0) and (form_data['end_frame'] != 0):
            if form_data['start_frame'] > form_data['end_frame']:
                self._errors["start_frame"] = ["End frame must bigger than Start Frame"]  # Will raise a error message
                del form_data['start_frame']
                del form_data['end_frame']
        return form_data