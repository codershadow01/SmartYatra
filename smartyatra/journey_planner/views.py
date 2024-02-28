from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim

# Create your views here.
def hpage(request):
    return render(request, "index.html")

class planner(View):

    def address_to_latlng(address):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return (None, None)

    def get(self,request):
        return render(request,'planner.html')
    
    def post(self,request):
<<<<<<< HEAD
        source = address_to_latlng(request.POST.get('source'))
        destination = address_to_latlng(request.POST.get('destination'))

=======
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        arr1 = nearby_points(source)
        arr2 = nearby_points(destination)

        res = search_algo(source,destination,arr1,arr2)

        return render(request,'planner.html',res)
>>>>>>> 6616d74310cbd649b1280add96f6e1959f938310


    def search_algo(source,destination,arr1,arr2):
        pass
    
    def nearby_points(node):
        pass

    def duration(source,destination):
        pass

    


def about(request):
    return render(request,"about.html")