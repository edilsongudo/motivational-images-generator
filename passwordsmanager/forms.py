from django import forms
from .models import *

class EntryForm(forms.ModelForm):

    key = forms.CharField(label='Type your master password again')

    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ['author']


class MasterPasswordForm(forms.ModelForm):

    last_master = forms.CharField(
        label='Last Master Password', required=False)
    master_confirm = forms.CharField(label='Master Password Confirm')

    class Meta:
        model = MasterPassword
        fields = ['last_master', 'master', 'master_confirm']


class MasterForm(forms.Form):
    key = forms.CharField(label='Master password')
