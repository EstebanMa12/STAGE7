"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist



class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                try:
                    profile = request.user.profile
                except ObjectDoesNotExist:
                    # Handle the case where the profile does not exist
                    profile = None
                if profile is None or not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), 
                                            reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response
