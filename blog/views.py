from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "all_posts_list"


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = "__all__"
    # success_url = reverse_lazy('home')

 
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "status"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')


