from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Post, Comment,UserProfile
from .forms import AddPostForm, UserRegistrationForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User



def home(request):
    if request.user.is_authenticated:
        return redirect('display_post')
    return render(request, 'home.html')



@login_required
def display_post(request):
   
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

 
    if request.method == 'POST':
        if 'like_post_id' in request.POST:
            post = get_object_or_404(Post, id=request.POST['like_post_id'])
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            return redirect('display_post')

        if 'comment_post_id' in request.POST:
            post = get_object_or_404(Post, id=request.POST['comment_post_id'])
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.user = request.user
                new_comment.save()
            return redirect('display_post')


    comment_forms = {post.id: CommentForm() for post in posts}

    return render(request, "posts.html", {
        "posts": posts,
        "comment_forms": comment_forms,
        "query": query  
    })



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
    post = get_object_or_404(Post, id=id)

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
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return HttpResponse("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('display_post')

    return render(request, 'delete.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            UserProfile.objects.create(user=new_user)

            return render(request, 'registration_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post.id)


@require_POST
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.user = request.user
        new_comment.save()
    return redirect('post_detail', post_id=post.id)


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(UserProfile, user=user)
    user_posts = Post.objects.filter(author=user).order_by('-created_at')
    return render(request, 'profile.html', {'profile_user': user, 'profile': profile , 'user_posts': user_posts})

def search_blogs(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render (request,'search_blogs.html' , {'results': results, 'query': query})