from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Vehicle,Signup

from django.http import HttpResponse
from dashboard.models import Vehicle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleSerializer

# Create your views here.


def index(request):
    errors = {}  
    if request.method == 'POST':
        # Retrieve form data
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_speed = request.POST.get('vehicle_speed')
        stationary_limit = request.POST.get('stationary_limit')
        mobile_no = request.POST.get('mobile_no')

        # Retrieve user object using the user's email stored in the session
        user_email = request.session.get('user_email')


        user = Signup.objects.get(email=user_email)


        if Vehicle.objects.filter(user=user, name=vehicle_name).exists():

            errors['vehicle_error'] = "Vehicle name already exists"
        
        else:


            # Create and save a new Vehicle instance
            vehicle = Vehicle.objects.create(
                user=user,
                name=vehicle_name,
                speed_limit=vehicle_speed,
                stationary_limit=stationary_limit,
                mobile_no=mobile_no
            )

            errors['success'] = 'Successfully Added'
        

    return render(request, 'dashboard/index.html',errors)



def VehiclePage(request):

    user_email = request.session.get('user_id')

    # Filter Vehicle objects related to the user's email
    Vehicle_Data = Vehicle.objects.filter(user=user_email)


    context = {
        "VehicleData":Vehicle_Data
    }

    return render(request,'dashboard/Vehicle.html',context)



def LocationPage(request,id):

    context = {
        'id':id
    }

    if request.method == 'POST':

        starting_address = request.POST.get('start_address')
        ending_address = request.POST.get('end_address')

        start_lattitude = request.POST.get('start_lat')
        start_langitude = request.POST.get('start_lng')

        end_lattitude  = request.POST.get('end_lat')
        end_longitude = request.POST.get('end_lng')

        vehicle = Vehicle.objects.get(pk=id)

        vehicle.starting_address = starting_address
        vehicle.ending_address = ending_address
        vehicle.starting_latitude = start_lattitude
        vehicle.starting_longitude = start_langitude
        vehicle.ending_latitude = end_lattitude
        vehicle.ending_longitude = end_longitude


        # Getting Lattitudes and Longituteds


        
        vehicle.save()

        return redirect('tasked-page')


    return render(request,'dashboard/location.html',context)




def Delete_Vehicle(request,id):

    vehicle = Vehicle.objects.get(pk=id)

    vehicle.delete()

    return redirect('vehicle-page')



def Tasked_Page(request):

    user_id = request.session.get('user_id')
    vehicles = Vehicle.objects.filter(user=user_id)



    return render(request,'dashboard/assigned_task.html',{'vehicles':vehicles})



def Map(request,id):

    return render(request,'dashboard/Map.html')





@api_view(['GET'])
def get_vehicles(request):
    if request.method == 'GET':
        # Retrieve the user's email from the session
        user_email = request.session.get('user_id')
        
        # Filter vehicles based on the user's email
        vehicles = Vehicle.objects.filter(user=user_email)
        
        # Serialize the filtered queryset
        serializer = VehicleSerializer(vehicles, many=True)
        
        # Return the serialized data
        return Response(serializer.data)





