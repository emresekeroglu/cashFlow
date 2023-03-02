from django.shortcuts import render
from django.http.response import HttpResponse
from .models import AccountBox, AccountAction

def index(request):
  accountsData = AccountBox.objects.all()
  accountActions = AccountAction.objects.all()
  return render(request, 'index.html', {'data': accountsData, 'actionData': accountActions})