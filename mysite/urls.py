"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib import admin,auth
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from magasin.views import ProductViewset
router=routers.SimpleRouter()
router.register('produit',ProductViewset,basename='produit')

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('admin/', admin.site.urls,name='admin'),
    path('magasin/',include('magasin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/Login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/Logout.html'), name = 'logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include(router.urls)),
    


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

