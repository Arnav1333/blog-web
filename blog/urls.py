from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('display',views.display_post,name='display_post'),
    path('add/',views.add_post,name = 'add_post'),
    path('edit/<int:id>',views.edit_post,name='edit_post'),
    path('delete/<int:id>',views.delete_post,name='delete_post'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(next_page='display_post'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]