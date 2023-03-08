from django.contrib import admin
from .models import AccountBox, Customer, AccountAction

class AccountBoxAdmin(admin.ModelAdmin):
  search_fields = ['accountName']
  list_display = ('accountName','accountAmount')
  
class CustomerAdmin(admin.ModelAdmin):
  search_fields = ['CustomerTitle']
  list_display = ('CustomerTitle','CustomerCode','CustomerPhone')
  
class AccountActionAdmin(admin.ModelAdmin):
  autocomplete_fields = ['accountName','CustomerTitle']
  list_display = ('CustomerTitle','accountName','in_out_flow','amount','description')
  
  
admin.site.register(AccountBox,AccountBoxAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(AccountAction,AccountActionAdmin)