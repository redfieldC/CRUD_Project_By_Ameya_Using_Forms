from django import forms
from .models import *

class MembersForm(forms.Form):
    class Meta:
        model = 'Members'
        fields = '__all__'