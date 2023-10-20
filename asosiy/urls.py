from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('bolimlar/', Bolimlar.as_view(), name='bolimlar'),
    path("mahsulotlar/<int:pk>/", Mahsulotlar.as_view(), name='mahsulotlar'),
    path('mahsulot/<int:pk>/', MahsulotView.as_view(), name='mahsulot'),
]

