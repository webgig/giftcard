"""prezzee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include,path
from django.views.generic.base  import TemplateView
from rest_framework import routers
from wallet import views
from cards import views as cardviews
from django.contrib.auth import views as auth_views

router = routers.SimpleRouter()
router.register(r'user', views.RegisterViewSet,'user')
router.register(r'me', views.UserProfileViewSet,'me')
router.register(r'cards', cardviews.CardViewSet,'cards')

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='index.html'),name='home'),
    path('login/', TemplateView.as_view(template_name='index.html'),name='login'),
    path('api/', include(router.urls)),
    path('api/auth/', views.AuthenticateUser.as_view()),
    path('admin/', admin.site.urls)
]
