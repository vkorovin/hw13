from django.urls import path

from server.apps.post.views import index

app_name = 'post'

urlpatterns = [
    path('hello/', index, name='hello'),
]
