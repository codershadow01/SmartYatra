from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
import pandas as pd
from .helper import find_nearest_points, search_algo
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
        print(routes)
        return render(request,'planner.html', {'routes': routes, 'source': source, 'destination': destination})

    


def about(request):
    return render(request,"about.html")

def nearby(request):
    return render(request,'nearby.html')