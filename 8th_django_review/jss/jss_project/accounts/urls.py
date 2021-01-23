from django.urls import path, include
import accounts.views

urlpatterns = [
    path('signup/', accounts.views.signup, name="signup"),
]