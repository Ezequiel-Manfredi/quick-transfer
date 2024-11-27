from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'balance']
  list_display_links = ['id']

admin.site.register(Account, AccountAdmin)