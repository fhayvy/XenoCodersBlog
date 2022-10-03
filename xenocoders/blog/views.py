from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import Author
from django.shortcuts import redirect


# Create your views here.

class AllPostsView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "all_posts_list"


class CreatePostView(CreateView):
    model = Post
    form = Author()
    template_name = "blog/post_form.html"
    fields = ["title", "created_on", "text", "status", "category"]
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(CreateView):
    model = Category
    template_name = "blog/add_category.html"
    fields = "__all__"
    success_url = reverse_lazy('home')

 
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


def CategoryView(request, cates):
    category_posts = Post.objects.filter(category=cates)


    context = {
        "category": cates,
        "category_posts": category_posts,
        }
    return render(request, "blog/category.html", context)


def contact_us(request):
    
    if request.method == "POST":
        message_name = request.POST['full-name']
        message_phone = request.POST['phone']
        message_email = request.POST['email']
        message = request.POST['message']

        context = {
            "message_name": message_name,
        }
        # SEND AN EMAIL THROUGH DJANGO
        send_mail(
            message_name,#subject
            message,#message
            settings.EMAIL_HOST_USER,#email_from
            [''],#recipient
            fail_silently=False,
        )
        

        
        return render(request, 'blog/contact_us.html', context)
        

    return render(request, 'blog/contact_us.html')
