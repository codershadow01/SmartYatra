from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
# from helper import find_nearest_points, search_algo
from django import forms
from .models import Nodes, Edges

# Create your views here.


# class RouteForm(forms.Form):
#     source = forms.ModelChoiceField(queryset=Nodes.object.all())
#     destination = forms.ModelChoiceField(queryset=Nodes.objects.all())

def hpage(request):
    return render(request, "index.html")

class planner(View):

    def get(self,request):
        nodes = Nodes.objects.all()
        return render(request,'planner.html',{'nodes':nodes, 'routes': 0})
    
    def post(self,request):
        source = request.POST.get('source')
        destination = request.POST.get('destination')
<<<<<<< Updated upstream
        arr1 = nearby_points(source)
        arr2 = nearby_points(destination)

        res = search_algo(source,destination,arr1,arr2)

        return render(request,'planner.html',res)


    def search_algo(source,destination,arr1,arr2):
        pass
    
    def nearby_points(node):
        pass

    def duration(source,destination):
        pass
=======
        print(request.POST)
        print(source)
        print(destination)
        return render(request,'planner.html', {'routes': 1})
>>>>>>> Stashed changes

    


def about(request):
    return render(request,"about.html")