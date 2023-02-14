from django.contrib import admin
from .models import AccountBox

class AccountBoxAdmin(admin.ModelAdmin):
  list_display = ('accountName','accountAmount')
  
  
admin.site.register(AccountBox,AccountBoxAdmin)