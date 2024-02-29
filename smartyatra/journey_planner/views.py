from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
# from helper import find_nearest_points, search_algo
from django import forms
from .models import Nodes, Edges


def hpage(request):
    return render(request, "index.html")

class planner(View):

    def get(self,request):
        nodes = Nodes.objects.all()
        return render(request,'planner.html',{'nodes':nodes, 'routes': 0})
    
    def post(self,request):
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        print(request.POST)
        print(source)
        print(destination)
        return render(request,'planner.html', {'routes': 1, 'source': source, 'destination': destination})

    


def about(request):
    return render(request,"about.html")