from django.urls import path
from .views import *

urlpatterns = [
    path('savat/', SavatlarView.as_view(), name='savat'),
    path('tanlangan/', TanlanganlarView.as_view(), name='tanlangan'),
    path('buyurtmalar/', BuyurtmalarView.as_view(), name='buyurtma'),
]
