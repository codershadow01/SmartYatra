from django.shortcuts import render

# Create your views here.
def hpage(request):
    return render(request, "hpage.html")

def planner(request):
    return render(request, "planner.html")