from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

class WriteView(generic.CreateView):
    template_name = 'blogs/post_new.html'
    model = Post
    fields = ['title', 'author', 'text']

    def get_initial(self):
        initial = super().get_initial()
        initial['author'] = self.request.user.get_username()
        return initial


class PostView(generic.ListView):
    template_name = 'blogs/posts.html'
    model = Post

class PostDetailView(generic.DetailView):
    template_name = 'blogs/post.html'
    model = Post
