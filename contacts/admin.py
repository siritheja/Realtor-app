from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id','listing','listing_id','name','email','phone','message','contact_date','user_id')
    list_display_links = ('id','name')
    search_fields = ('name','email','listing')
    list_per_page = 25

admin.site.register(Contact, ContactsAdmin)