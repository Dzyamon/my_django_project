"""
URL configuration for my_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from myapp1 import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about, kwargs={"name":"Tom", "age": 38}),
    path('', views.index, name='home'),
    path('index1', views.index1),
    path('index2', views.index2),
    path('index3', views.index3),
    path("user", views.user),
    path("user2/", views.user2), #http://127.0.0.1:8000/user2/?name=Tom&age=22
    path("user/<name>", views.user),
    path('user/<str:name>/<int:age>', views.user),
    path("products/<int:id>/", include(product_patterns)),
    path("set", views.set), #http://127.0.0.1:8000/set?username=Dzyamon
    path("get", views.get), #http://127.0.0.1:8000/get
]
