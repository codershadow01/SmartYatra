from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
import pandas as pd
from .helper import find_nearest_points, search_algo, find_nearby_services
from django import forms
from .models import Nodes, Edges
import json


def hpage(request):
    return render(request, "index.html")

class planner(View):

    def get(self,request):
        nodes = Nodes.objects.all()
        return render(request,'planner.html',{'nodes':nodes, 'routes': 0})
    
    def post(self,request):
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        
        def get_name(node):
            return node.name

        df = pd.DataFrame(Nodes.objects.all(),columns=["Nodes"])
        df['Name'] = df['Nodes'].apply(get_name)
        src = df[df['Name'] == (source)]
        dest = df[df['Name'] == (destination)]
        lat1 = src.iloc[0]['Nodes'].lat
        lon1 = src.iloc[0]['Nodes'].lon

        lat2 = dest.iloc[0]['Nodes'].lat
        lon2 = dest.iloc[0]['Nodes'].lon

        arr1 = find_nearest_points(lat1, lon1, precision=7)
        arr2 = find_nearest_points(lat2, lon2, precision=7)

        routes = search_algo(lat1, lon1, lat2, lon2, arr1, arr2)
        json_arr1 = json.dumps(routes)
        
        return render(request,'planner.html', {'routes': routes, 'source': source, 'destination': destination, 'json_data':json_arr1})


def about(request):
    return render(request,"about.html")


class nearby(View):
    def get(self, request):
        nodes = Nodes.objects.all()
        return render(request,'nearby.html',{'nodes':nodes, 'services': 0})
    
    def post(self, request):
        location = request.POST.get('location')

        def get_name(node):
            return node.name

        df = pd.DataFrame(Nodes.objects.all(),columns=["Nodes"])
        df['Name'] = df['Nodes'].apply(get_name)
        location = df[df['Name'] == (location)]
        lat = location.iloc[0]['Nodes'].lat
        lon = location.iloc[0]['Nodes'].lon

        arr1 = find_nearby_services(lat, lon, precision=5)
        services = [{'bus':arr1[0]}, {'auto':arr1[1]}]
        json_arr1 = json.dumps(services)
        print(json_arr1)
        return render(request,'nearby.html', {'services':json_arr1, 'location': location.iloc[0]['Nodes'].name})