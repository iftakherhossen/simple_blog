from django.urls import path
from . import views

urlpatterns = [
    path('@<str:username>/', views.author_profile, name='author'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),    
    path('profile/forgot_password/', views.forgot_password, name='forgot_password'),
]