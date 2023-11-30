"""User Forms"""
# Django
from django import forms

# Models

class ProfileForm(forms.Form):
    """Profile form."""
    
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    
    picture = forms.ImageField()

class SignupForm(forms.Form):
    """Sign up form"""
    username = forms.CharField(min_length = 4,max_length = 50)
    
    password = forms.Charfield(max_length = 70, 
                            widget = forms.PasswordInput())
    password_confirmation = forms.Charfield(max_length, 
                                            widget = forms.PasswordInput())
    
    first_name = forms.Charfield(min_length = 2, max_length = 50 )
    last_name = forms.Charfield(min_length = 2, max_length = 50 )
    
    email = forms.Charfield(min_length = 6, max_length = 70, widget = forms.emailInput() )    
    