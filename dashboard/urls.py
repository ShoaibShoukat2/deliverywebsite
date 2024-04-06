from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='dash-index'),
    path('vehicle/',Vehicle,name='vehicle-page'),
    path('location/',LocationPage,name='location-page'),
    path('AssignedTask/',Tasked_Page,name='tasked-page')

]






