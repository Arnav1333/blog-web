from django.shortcuts import render,redirect,HttpResponse
from .models import Post
from .forms import AddPostForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def display_post(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"posts.html",{"posts":posts})

@login_required
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('display_post')
    else:
        form = AddPostForm()
    
    return render(request, "add.html", {"form": form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id)
    if post.author != request.user:
        return HttpResponse("You are not allowed to edit this post.")

    if request.method == "POST":
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('display_post')
    else:
        form = AddPostForm(instance=post)  

    return render(request, 'edit.html', {"form": form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    if post.author != request.user:
        return HttpResponse("You are not allowed to delete this post.")
    if request.method == 'POST':
        post.delete()
        return redirect('display_post')
    return render(request, 'delete.html', {'post':post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

   