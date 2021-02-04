from django import forms
from upload_app.models import *


class CreateFilesForm(forms.ModelForm):
    class Meta:
        model = CreateFiles
        exclude = ['user_id']
