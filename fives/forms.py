from django import forms
from .models import UserProfile, Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = ('team',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ('comment',)
