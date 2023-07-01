from typing import final
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


from .models import CustomUser, Post


@final
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


@final
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


@final
class PostCreationForm(ModelForm):
     class Meta:
        model = Post
        fields = ['title', 'body' ]

