#Django
from django.http import HttpResponse, JsonResponse

#Utilities
from datetime import datetime

def hello_world(request):
    """RETURNING A GREETING"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')

def sorted(request):
    numbers = sorted([int(x) for x in request.GET['numbers'].split(',')])
    print(numbers)
    return JsonResponse(
        {'numbers': numbers,
        'message': 'Integers sorted successfully'},
        json_dumps_params={'indent': 4}
    )
    
def say_hi(request, name, age):
    """RETURNING A GREETING"""
    
    message = f'Sorry {name}, you are not allowed here' if age < 12 else f'Hello {name}! Welcome to Instagram Clone'
    return HttpResponse(message)