from django.urls import path
from . import views

urlpatterns = [
    path('signup1/', views.signup1, name="signup1"),
    path('login1/', views.login1, name="login1"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]