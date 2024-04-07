from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at','remember_me')
    search_fields = ('name', 'email',)
    list_filter = ('created_at',)



