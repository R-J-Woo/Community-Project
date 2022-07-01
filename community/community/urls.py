"""community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user.views import home, Register, Login, MyPage, logout
from post.views import PostList, PostRegister, PostDetail
from comment.views import CommentCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', logout),
    path('board/', PostList.as_view()),
    path('board/register/', PostRegister),
    path('board/<int:pk>/', PostDetail.as_view()),
    path('comment/create/', CommentCreate.as_view()),
    path('mypage/', MyPage.as_view())
]
