from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
def hpage(request):
    return render(request, "index.html")

class planner(View):
    def get(self,request):
        return render(request,'planner.html')
    
    def post(self,request):
        source = request.POST.get('source')
        destination = request.POST.get('destination')


    def search_algo(source,destination,arr1,arr2):
        pass
    
    def nearby_points(node):
        pass

    def duration(source,destination):
        pass

def about(request):
    return render(request,"about.html")