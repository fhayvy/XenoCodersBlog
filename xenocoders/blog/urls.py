from django.urls import path
from .views import contact, AllPostsView, CreatePostView, PostDetailView, PostUpdateView, PostDeleteView, AddCategoryView, CategoryView
from .forms import ContactForm
from . import views


urlpatterns = [
    path('', AllPostsView.as_view(), name="home"),
    path('add_post/', CreatePostView.as_view(), name="add_post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post"),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name="update_post"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="delete_post"),
    path('contact_us/', views.contact, name="contact"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cates>/', CategoryView, name="category"),  
]