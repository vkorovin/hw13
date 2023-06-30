from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.utils.text import slugify
from .models import Post
from .forms import PostCreationForm


class PostList(ListView):
    queryset = Post.objects.prefetch_related('author')
    context_object_name = 'post_list'


class PostView(DetailView):
    model = Post
    template_name = 'post/post_view.html'

class PostCreate(CreateView):
    form_class = PostCreationForm
    template_name = 'post/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)



def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'post/index.html')
# Create your views here.
