from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'page-index.html')

class LoginsizView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class Bolimlar(View):
    def get(self, request):
        return render(request, 'page-category.html')

class Mahsulotlar(View):
    def get(self, request):
        return render(request, 'page-listing-grid.html')

class MahsulotView(View):
    def get(self, request):
        return render(request, 'page-detail-product.html')