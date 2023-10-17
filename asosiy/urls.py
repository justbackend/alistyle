from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('bolimlar/', Bolimlar.as_view(), name='bolimlar'),
    path("mahsulotlar/", Mahsulotlar.as_view(), name='mahsulotlar'),
    path('mahsulot/', MahsulotView.as_view(), name='mahsulot'),
]

