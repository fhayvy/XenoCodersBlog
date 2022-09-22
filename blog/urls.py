from django.urls import path
from .views import HomeView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('add_post/', PostCreateView.as_view(), name="add_post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post"),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name="update_post"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="delete_post"),

]