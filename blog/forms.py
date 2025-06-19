from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        