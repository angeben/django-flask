from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.quotes, name="quotes"),
    path('quotes/category/<int:category_id>', views.quotes, name="quotes-filter"),
    path('quotes/<int:id>/', views.get_quote, name="get-quote"),
    path('quotes/<int:id>/edit/', views.edit_quote, name="update-quote"),
    path('quotes/<int:id>/delete/', views.delete_quote, name="delete-quote"),
    path('quotes/create/', views.create_quote, name="create-quote")
]
