from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import Author
from django.shortcuts import redirect
from .forms import ContactForm


# Create your views here.

class AllPostsView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "all_posts_list"

#     def get_context_data(self, *args, **kwargs):
#         # post_title = Post.objects.filter(title)
#         stuff = get_object_or_404(Post, id=self.kwargs[self.title])

#         context = super(AllPostsView, self).get_context_data(*args, **kwargs)

#         context["post_title"] = stuff
#         return context

# def AllPostsView(request):
#     return render(request, "blog/home.html")


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


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "New Message" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'hi@imrvon.com', ['hi@imrvon.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("contact")
      
	form = ContactForm()
	return render(request, "blog/contact_us.html", {'form':form})