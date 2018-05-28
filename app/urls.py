"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

from posts.api.views import PostsViewSet
from user.api.views import UserViewSet
from comments.api.views import CommentsViewSet

swagger_view = get_swagger_view(title='Blog X Django')

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('posts', PostsViewSet)
router.register('comments', CommentsViewSet)

urlpatterns = [
    path('', swagger_view),
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
]
