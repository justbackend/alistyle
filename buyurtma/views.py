from django.shortcuts import render
from django.views import View
class SavatlarView(View):
    def get(self, request):
        return render(request, 'page-shopping-cart.html')

class TanlanganlarView(View):
    def get(self, request):
        return render(request, 'page-profile-wishlist.html')

class BuyurtmalarView(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')