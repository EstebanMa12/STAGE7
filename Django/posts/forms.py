"""Post forms """

# Django 
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model form."""
    
    class Meta:
        """Form settings."""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
