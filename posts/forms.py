from django import forms
from django.forms.widgets import TextInput
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'connects', 'last_image_downloaded',
        'number_of_posts_created', 'number_of_posts_downloaded',
        'code', 'recommended_by', 'ref_code_clicks', 'money']

        widgets = {
            'primary_text_color': TextInput(attrs={'type': 'color'}),
            'brand_name_font_color': TextInput(attrs={'type': 'color'})
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
