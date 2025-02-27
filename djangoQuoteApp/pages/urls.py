from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('page/<str:slug>', views.page, name="page")
]
