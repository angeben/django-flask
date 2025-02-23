"""
URL configuration for djangoDemoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.helloWorld, name="helloWorld"),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('say-hi/', views.sayHi, name="sayHi"),
    path('say-hi/<str:name>/', views.sayHi, name="sayHi"),
    path('quotes/', views.quotes, name="quotes"),
    path('quotes/<int:id>/', views.get_quote, name="get-quote"),
    path('quotes/<int:id>/edit/', views.edit_quote, name="update-quote"),
    path('quotes/<int:id>/delete/', views.delete_quote, name="delete-quote"),
    path('quotes/create/', views.create_quote, name="create-quote")
]
