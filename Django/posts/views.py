#Django
from datetime import datetime
from django.shortcuts import render

#Local
from django.http import HttpResponse

posts = [
    {
        'name': 'Clifford Howell',
        'user': 'clifford',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
    
]
# Create your views here.
def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append("""
                        <p><strong>{name}</strong></p>
                        <p><small>{user} - <i>{timestamp}</i></small></p>
                        <figure><img src="{picture}"/></figure>
                        """.format(**post))
    return HttpResponse('<br>'.join(content))