from django.db import models
# Create your models here.
import textwrap
from typing import final

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.conf import settings
from django.urls import reverse



@final
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@final
class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(null=False, unique=True)
    body =  models.TextField()
    author =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_view', kwargs={"slug": self.slug})
