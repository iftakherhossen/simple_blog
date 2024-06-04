from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.view_post, name='view_post'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
]