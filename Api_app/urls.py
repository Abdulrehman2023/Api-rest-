"""API_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .views import new1,new_details, article, CustomAuthToken,registeruser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
from Api_app  import views

from rest_framework import routers
app_name = "Api_app"
router = routers.DefaultRouter()
router.register(r"APiDefaultViewSet", views.APiDefaultViewSet, "APiDefaultViewSet")



urlpatterns = [
    path('api/',csrf_exempt(new1)),
    path('details/<int:pk>/',new_details),
    path('class_api/',article.as_view()),
   path('api-token-auth/', CustomAuthToken.as_view()),
   path('registeruser/', registeruser.as_view()),
   path('modelview/', registeruser.as_view()),
   path("", include(router.urls)),
   
   

  
]
