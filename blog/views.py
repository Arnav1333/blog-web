from django.shortcuts import render,redirect
from .models import Post
from .forms import AddPostForm


# Create your views here.

def display_post(request):
    posts = Post.objects.all()
    return render(request,"posts.html",{"posts":posts})


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_post')
    else:
        form = AddPostForm()
    
    return render(request, "add.html", {"form": form})

