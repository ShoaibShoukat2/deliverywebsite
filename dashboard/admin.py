from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at','remember_me')
    search_fields = ('name', 'email',)
    list_filter = ('created_at',)



@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'speed_limit',
        'stationary_limit', 
        'mobile_no',
        'starting_address',
        'ending_address',
        'starting_latitude',
        'starting_longitude',
        'ending_latitude',
        'ending_latitude'
        )



