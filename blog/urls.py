"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import blogpost.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogpost.views.home, name="home"),
    path('blog/<int:blog_id>', blogpost.views.detail, name="detail"),
    path('blog/new', blogpost.views.new, name="new"),
    path('blog/create', blogpost.views.create, name="create"),
    path('blog/delete/<int:blog_id>', blogpost.views.delete, name = "delete"),
    path('blog/edit/<int:blog_id>', blogpost.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>', blogpost.views.update, name="update"),

    path('makecomment/<int:blog_id>', blogpost.views.make_comment, name='make_comment'),
    path('deletecomment/<int:blog_id>/<int:comment_id>', blogpost.views.delete_comment, name='delete_comment'),
]
