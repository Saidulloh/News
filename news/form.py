from django import forms
from django.forms.widgets import TextInput
from .models import *

class SocialSidebarForm(forms.ModelForm):
    class Meta:
        model = SocialSidebar
        fields = '__all__'
        widgets = {
            'background': TextInput(attrs={'type': 'color'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length = 255)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 255)
    message = forms.CharField(max_length = 1000)


class AddPostsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__' 