from django.shortcuts import render

# Create your views here.
def hpage(request):
    return render(request, "index.html")

def planner(request):
    return render(request, "planner.html")

def about(request):
    return render(request,"about.html")