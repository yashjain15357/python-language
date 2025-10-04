"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import *
from veg.views import *
# from account.views import *
from django.conf import settings
from django.conf.urls.static import static

# use for routing
urlpatterns = [
    path('',home,name="home" ),
    path('about/',about,name="about" ),
    path('contact/',contact,name="contact" ),
    path('recipes/',recp,name="recipes"),
    path('delete_recp/<int:id>/',delete_recp,name="delete_recp"),
    path('update_recp/<int:id>/',update_recp,name="update_recp"),
      
    path('login/',login ,name="login"),
    path('register/', register ,name='register' ),
    # path("success/",success_full,name="success_full"),

    path('admin/', admin.site.urls),
    path('logout/', logout_page , name= 'logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)