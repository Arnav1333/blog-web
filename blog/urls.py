from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('display', views.display_post, name='display_post'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(next_page='display_post'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('profile/<str:username>/', views.profile_view, name='user_profile'),
    path('search/blogs/', views.search_blogs, name='search_blogs'),
    path('search/users/', views.search_users, name='search_users'),
    path('save-post/<int:post_id>/', views.save_post, name='save_post'),
    path('saved-posts/', views.saved_posts_list, name='saved_posts'),



]
