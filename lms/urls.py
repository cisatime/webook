"""lms URL Configuration

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
from django.conf.urls.static import static
from app01 import views

from django.conf.urls import url

urlpatterns = [
    # 管理员账户登陆
    path('admin/', admin.site.urls),
    
    # 个人主页
    path('publisher_list/', views.publisher_list),
    path('add_publisher/', views.add_publisher),
    path('drop_publisher/', views.drop_publisher),
    path('edit_publisher/', views.edit_publisher),
    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('drop_book/', views.drop_book),
    path('edit_book/', views.edit_book),
    #
    path('customer_serivice/',views.customer_serivice),
    path('success_question/',views.success_question),
    path('books_shop/', views.books_shop),
    path('social_contact/', views.social_contact),
    # 注册
    path('register/', views.register),
    url(r'^register/', views.register),
    url(r'^register2/', views.register2),
    path('register2/', views.register2),
    #登录
    url(r'^login/', views.login),
    path('login/', views.login),
    path('login_phone/', views.login_phone),
    path('logout/',views.logout),
    # 主页
    path('books_shop/', views.books_shop),
]
