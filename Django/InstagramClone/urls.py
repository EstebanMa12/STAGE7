"""
URL configuration for InstagramClone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from InstagramClone.views import views as local_views

from posts import views as posts_views
from users import views as user_views

  
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world, name = 'hello_world'),
    path('sorted/', local_views.sorted, name = 'sort'),
    path('hi/<str:name>/<int:age>/', local_views.say_hi, name  'hi'),
    path('posts/', posts_views.list_posts, name = 'feed'),
    path('users/login/', users_views.login_view, name = 'login')
   
]

if settings.DEBUG:
     # La función static() se utiliza para añadir rutas URL para servir archivos estáticos durante el desarrollo. Los archivos estáticos son todos tus archivos CSS y JavaScript, imágenes, y cualquier otro archivo que no sea Python que necesites para tu aplicación web
    # En este caso, static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) está añadiendo rutas para servir archivos de medios durante el desarrollo. Los archivos de medios son, por ejemplo, las imágenes subidas por los usuarios de tu aplicación web.

    # settings.MEDIA_URL es la URL que Django usará para referirse a los archivos de medios. settings.MEDIA_ROOT es la ubicación absoluta del directorio en tu sistema de archivos donde Django almacenará los archivos de medios.
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
