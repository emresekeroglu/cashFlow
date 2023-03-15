from django.shortcuts import render
from .models import AccountBox, AccountAction
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  accountsData = AccountBox.objects.all()
  accountDatas = AccountAction.objects.all()
  return render(request, 'index.html', {'data': accountsData, 'actionData': accountDatas})