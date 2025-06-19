from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.title}"
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100,blank=True)

    def avatar_url(self):
        name = self.user.username or "User"
        return f"https://ui-avatars.com/api/?name={name}&background=random"

    def __str__(self):
        return f"{self.user.username}'s Profile"

class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','post')
    
