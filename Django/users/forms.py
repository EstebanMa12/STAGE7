"""User Forms"""

from django import forms

# Models

class ProfileForm(forms.Form):
    """Profile form."""
    
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    
    picture = forms.ImageField()
    
    def clean(self):
        """Clean data"""
        data = super().clean()
        
        phone_number = data['phone_number']
        
        if len(phone_number) < 10:
            raise forms.ValidationError('Phone number must be at least 10 characters long')
        
        return data