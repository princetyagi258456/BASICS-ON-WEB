"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('removepunc',views.removepunc,name="remopun"),
    path('capitalizefirst',views.capfirst,name="capfirst"),
    path('newlineremove',views.newlineremove,name="newlineremove"),
    path('spaceremove',views.spaceremove,name="spaceremove"),
    path('charcount',views.charcount,name="charcount"),



    path('login/',views.index1,name='index1'),
    path('login1/',views.index2,name='index2'),
]
