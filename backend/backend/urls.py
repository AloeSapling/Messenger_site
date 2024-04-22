from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend_app import views
from django.contrib.auth import views as auth_views
from backend_app.forms import CustomAuthenticationForm
router = DefaultRouter()
router.register(r'message', views.MessageViewSet, basename='message')
router.register(r'user', views.UsersViewSet, basename='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
