from django.shortcuts import render

from .models import Vehicle

# Create your views here.


def index(request):

    if request.method == 'POST':
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_speed = request.POST.get('vehicle_speed')
        stationary_limit = request.POST.get('stationary_limit')
        vehicle_no = request.POST.get('vehicle_no')




    return render(request,'dashboard/index.html')


def Vehicle(request):



    return render(request,'dashboard/Vehicle.html')




def LocationPage(request):
    return render(request,'dashboard/location.html')



def Tasked_Page(request):
    return render(request,'dashboard/assigned_task.html')



