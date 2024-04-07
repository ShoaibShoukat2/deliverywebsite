from django.shortcuts import render
from dashboard.models import Signup
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password  # Import make_password
# Create your views here.


def index(request):
    return render(request,'index.html')



def signup(request):
    context = {}  # Initialize an empty context dictionary
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        remember_me = request.POST.get('remember_me')
        
        if Signup.objects.filter(email=email).exists():
            context['error_message'] = 'User with this email already exists. Please use a different email.'
            context['redirect_url'] = 'signup'

        else:

            hashed_password = make_password(password)


            # Create a new Signup object and save it to the database
            new_signup = Signup.objects.create(
                name=first_name,
                email=email,
                password=hashed_password,
                remember_me=remember_me 
            )


            context['success_message'] = 'submitted successfully'
            context['redirect_url'] = 'login'

        



    return render(request, 'signup.html',context) 











def login(request):
    return render(request,'login.html')



def contact(request):

    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')

    