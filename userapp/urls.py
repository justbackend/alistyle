from django.urls import path
from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('tasdiqlash/', Tasdiqlash.as_view(), name='tasdiqlash'),
]

