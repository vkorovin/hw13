from typing import final
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from django.utils.text import slugify
from .models import Post
from .forms import PostCreationForm
from .utils import random_string

@final
class PostList(ListView):
    queryset = Post.objects.prefetch_related('author')
    context_object_name = 'post_list'


@final
class PostView(DetailView):
    model = Post
    template_name = 'post/post_view.html'


@final
class PostCreate(CreateView):
    form_class = PostCreationForm
    template_name = 'post/post_form.html'
    model = Post

    def form_valid(self, form):
        slug =slugify(form.instance.title)

        if self.model.objects.filter(slug=slug).exists():
            slug = slugify(form.instance.title + ' ' + random_string(2,2))

        form.instance.author = self.request.user
        form.instance.slug = slug
        return super().form_valid(form)


@final
class PostUpdate(UpdateView):
    model = Post
    fields = [ 'title','body' ]
    template_name = 'post/post_update.html'


@final
class PostDelete(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy("post_list")

def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'post/index.html')
# Create your views here.
