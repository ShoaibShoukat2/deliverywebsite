from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'created_at','remember_me')
    search_fields = ('name', 'email', 'address')
    list_filter = ('created_at',)



