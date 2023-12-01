"""User Forms"""
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):
    """Profile form."""
    
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    
    picture = forms.ImageField()

class SignUpForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(
        label= False,
        widget= forms.TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control',
            'required':True
        }),
        min_length=4, 
        max_length=50)
    
    password = forms.CharField(
        label= False,
        widget= forms.PasswordInput(attrs={
            'placeholder':'Password',
            'class':'form-control',
            'required':True,
            }),
        max_length=70,
        )
    password_confirmation = forms.CharField(
        label= False,
        widget= forms.PasswordInput(attrs={
            'placeholder':'Password Confirmation',
            'class':'form-control',
            'required':True,
            }),
        max_length=70, )
    
    first_name = forms.CharField(
        label= False,
        widget= forms.TextInput(attrs={
            'placeholder':'First Name',
            'class':'form-control',
            'required':True,
            }),
        min_length=2, 
        max_length=50)
    last_name = forms.CharField(
        label= False,
        widget= forms.TextInput(attrs={
            'placeholder':'Last Name',
            'class':'form-control',
            'required':True,
            }),
        min_length=2, 
        max_length=50)
    
    email = forms.EmailField(
        label= False,
        widget= forms.EmailInput(attrs={
            'placeholder':'email',
            'class':'form-control',
            'required':True,
            }),
        min_length=6, 
        max_length=70, )
    
    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        username_taken = User.objects.filter(username = username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username
    
    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        
        passwd = data['password']
        passwd_confirmation = data['password_confirmation']
        
        if passwd != passwd_confirmation:
            raise forms.ValidationError('Passwords do not match')
        return data
    
    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')
        
        user = User.objects.create_user(**data)
        user.save()
        
        profile = Profile(user=user)
        profile.save()