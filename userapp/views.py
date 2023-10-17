from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from random import randint
from eskiz.client import SMSClient
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

class Register(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
    def post(self, request):
        user = User.objects.create_user(
            username=request.POST.get("phone"),
            password=request.POST.get("p1")
        )
        kod = randint(100000, 999999)
        Profile.objects.create(
            user = user,
            sms_kod=str(kod),
            shahar=request.POST.get("shahar"),
            davlat=request.POST.get('davlat'),
            ism = request.POST.get("ismi") + " " + request.POST.get("f"),
            tel_raqam=request.POST.get("phone"),
            jins = request.POST.get("gender")
        )
        client = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email="1997abdulhamid@gmail.com",
            password="j1YS958itCXn4uEJbZX9bbD7IIp9DOdNbxQ6psdr",
        )

        client._send_sms(
            phone_number=request.POST.get("phone"),
            message=f"{request.POST.get('ismi')} sizning ko'dingiz: {kod}"
        )

        return redirect("tasdiqlash")

class Tasdiqlash(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        profil = Profile.objects.filter(
            sms_kod=request.POST.get("kod"),
            tel_raqam=request.POST.get("tel"),
        )
        if len(profil) == 0:
            return redirect("tasdiqlash")
        profil = profil[0]
        profil.tasdiqlangan = True
        profil.save()
        return redirect("login")
