from django.urls import path, include
import accounts.views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', accounts.views.signup, name="signup"),
    path('login/', accounts.views.MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]