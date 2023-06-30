from django.urls import path
from server.apps.post.views import index, PostCreate, PostView


app_name = 'post'

urlpatterns = [
    path('hello/', index, name='hello'),
    path('create/', PostCreate.as_view()),
    path('<slug>/', PostView.as_view(),name='post_view'),
]
