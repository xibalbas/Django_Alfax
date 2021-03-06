from django.contrib import admin
from .models import *



# class IncomeAdmin(admin.ModelAdmin):
#     list_display = ('title','amount','user','jpub_date')
#     list_filter = ('user','pub_date')
#     search_fields= ('title', 'description')

# class ExpenceAdmin(admin.ModelAdmin):
#     list_display = ('title','amount','user','jpub_date')
#     list_filter = ('user','pub_date')
#     search_fields= ('title', 'description')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('nameandfamily','companyname','mobile','phone','address')
    list_filter = ('nameandfamily','companyname','mobile','phone','address')
    search_fields = ('nameandfamily','companyname','mobile','phone','address')


admin.site.register(invoice)
admin.site.register(Contacts,ContactsAdmin)

admin.site.register(buy)
admin.site.register(sell)
admin.site.register(UserProfile)
