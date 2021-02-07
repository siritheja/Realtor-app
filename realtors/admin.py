from django.contrib import admin
from .models import Realtor

# Register your models here.
class Realtoradmin(admin.ModelAdmin):
    list_display= ('id','name','phone','email','is_mvp','hire_date')
    list_display_links= ('id','name','hire_date')
    list_editable = ('phone','email','is_mvp')
    list_filter=('is_mvp',)
    search_fields=('name',)
    list_per_page = 20

admin.site.register(Realtor,Realtoradmin)