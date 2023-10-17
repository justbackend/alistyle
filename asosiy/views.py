from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'page-user-login.html')
        return render(request, 'page-user-login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

    def post(self, request):
        pass