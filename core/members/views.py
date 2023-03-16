from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from members.recaptcha import recaptcha_check

def all_the_values(dictionary):
   for keys , values in dictionary.items():
      if isinstance(values, dict):
         for x in all_the_values(values):
            yield x
      else:
         yield values

def login_user(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        recaptcha_response_result = recaptcha_check(recaptcha_response)
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password=password)
        if recaptcha_response_result is True:
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, ("Kullanıcı Adı veya Parola Hatalı. Lütfen Tekrar Deneyiniz!"))
                return redirect('home')
        else:
            messages.error(request, ("reCaptcha İşlemi Hatalı!"))
            return redirect('home')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Güvenli Çıkış Yapıldı."))
    return redirect('home')