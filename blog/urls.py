from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.display_post,name='display_post'),
    path('add/',views.add_post,name = 'add_post')
]