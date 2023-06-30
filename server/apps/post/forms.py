from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.utils.text import slugify

from .models import CustomUser, Post


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class PostCreationForm(ModelForm):
     class Meta:
        model = Post
        fields = ['title', 'body' ]

