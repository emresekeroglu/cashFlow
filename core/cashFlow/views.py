from django.shortcuts import render
from django.http.response import HttpResponse
from .models import AccountBox

def index(request):
  accountsData = AccountBox.objects.all()
  return render(request, 'index.html', {'data': accountsData})