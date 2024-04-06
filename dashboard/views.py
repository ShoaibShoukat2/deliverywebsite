from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'dashboard/index.html')





def Vehicle(request):
    return render(request,'dashboard/Vehicle.html')




def LocationPage(request):
    return render(request,'dashboard/location.html')

