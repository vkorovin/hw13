from django.urls import path
from server.apps.post.views import index, PostCreate, PostView, PostUpdate, PostDelete


app_name = 'post'

urlpatterns = [
    path('hello/', index, name='hello'),
    path('create/', PostCreate.as_view()),
    path('<slug>/', PostView.as_view(),name='post_view'),
    path('<slug>/update', PostUpdate.as_view(),name='post_update'),
    path('<slug>/delete', PostDelete.as_view(),name='post_delete')
]
