from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='dash-index'),
    path('vehicle/',VehiclePage,name='vehicle-page'),
    path('location/<int:id>',LocationPage,name='location-page'),
    path('location/delete/<int:id>/',Delete_Vehicle,name='delete-vehicle'),
    path('AssignedTask/',Tasked_Page,name='tasked-page'),
    path('AssignedTask/map/<int:id>',Map,name='map-page'),

      #API Endpoints


    path('api/vehicles/',get_vehicles,name="apis-page")
    
    
]


