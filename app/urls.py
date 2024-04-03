from django.urls import path
from .views import *

urlpatterns = [

    path('',index,name="index-pgae"),
    path('signup/',signup,name="signup-page"),
    path('login/',login,name="login-page"),
    path('contact/',contact,name="contact-page"),
    path('about/',about,name="about-page")
]


