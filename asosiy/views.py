from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class HomeView(View):
    def get(self, request):
        content = {
            'bolimlar': Bolim.objects.all()[:7],
            "mahsulotlar": Mahsulot.objects.all()
        }
        return render(request, 'page-index.html', content)

class LoginsizView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class Bolimlar(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()
        }
        return render(request, 'page-category.html', content)

class Mahsulotlar(View):
    def get(self, request, pk):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request, 'page-listing-grid.html', content)

class MahsulotView(View):
    def get(self, request, pk):
        content = {
            "izohlar": Izoh.objects.filter(mahsulot_id=pk),
            "mahsulot": Mahsulot.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html', content)

