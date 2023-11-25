from django import forms
from .models import UserGroups, Message


class GroupForm(forms.ModelForm):
    class Meta:
        model = UserGroups
        fields = ['name', 'description']
