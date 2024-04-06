from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='dash-index'),
    path('vehicle/',Vehicle,name='vehicle-page')

]



