from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
import pandas as pd
from .helper import find_nearest_points, search_algo, find_nearby_services
from django import forms
from .models import Nodes, Edges
import json
from django.http import JsonResponse

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
        if(src.empty):
            return render(request,'planner.html', {'routes': [], 'routes_list':[]})
        dest = df[df['Name'] == (destination)]
        if(dest.empty):
            return render(request,'planner.html', {'routes': [], 'routes_list':[]})
        lat1 = src.iloc[0]['Nodes'].lat
        lon1 = src.iloc[0]['Nodes'].lon

        lat2 = dest.iloc[0]['Nodes'].lat
        lon2 = dest.iloc[0]['Nodes'].lon

        arr1 = find_nearest_points(lat1, lon1, precision=7)
        arr2 = find_nearest_points(lat2, lon2, precision=7)

        routes = search_algo(lat1, lon1, lat2, lon2, arr1, arr2)
        
        route_dict = {}
        routes_list = []
        # travel_time = routes[1]
        # travel_time = json.dumps(travel_time)
        if len(routes)==0:
            return render(request,'planner.html', {'routes': [], 'routes_list':[],'message':"No public Routes exist yet!"})
        for route in routes[0][0]:
            mode = route[0]
            node1 = {
                "node_name":route[1],
                "lat":route[2],
                "lon":route[3]
            }
            node2    = {
                "node_name":route[4],
                "lat":route[5],
                "lon":route[6]
            }
            temp_dict = {"mode":mode,"node1":node1,"node2":node2}
            routes_list.append(temp_dict)
        
        routes_list = json.dumps(routes_list)

        total_time = routes[0][1]
        w_time = round(total_time * 2)
        b_time = round(total_time * 1.5)
        c_time = round(total_time * 0.5)
        w_h = w_time // 60
        w_m = w_time % 60
        b_h = b_time // 60 
        b_m = b_time % 60
        c_h = c_time // 60
        c_m = c_time % 60

        walk_time = f"{w_h} hr {w_m} min"
        bicycle_time = f"{b_h} hr {b_m} min"
        cab_time = f"{c_h} hr {c_m} min" 
          
        # routes_list = str(routes_list)

        # print("Travel time : ",travel_time)
        # print(routes_list)
        # print(type(routes_list))
        # print("hello")   

        return render(request,'planner.html', {'routes': routes, 'source': source, 'destination': destination,'routes_list':routes_list, 'walk_time':walk_time, 'bicycle_time':bicycle_time, 'cab_time':cab_time })


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
        
        # with open('data.json', 'w') as f:
        #     json.dump(arr1, f)
        # for i in arr1:
        res = []
        for service in arr1:
            mode=service[0]
            node={
                "node_name":service[1],
                "lat":service[2],
                "lon":service[3]
            }
            temp_dic={'mode':mode,'node':node}
            res.append(temp_dic)

        res = json.dumps(res)
        return render(request,'nearby.html', {'services': res,'list':arr1, 'location': location.iloc[0]['Nodes'].name})
    
def login(request):
    return render(request,'login.html')

def personalized(request):
    return render(request, 'personalized.html')