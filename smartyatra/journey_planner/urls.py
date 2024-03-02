from django.urls import path
from . import views
from .views import planner,hpage,about,nearby

urlpatterns = [
    path('planner/',planner.as_view(),name="planner"),
    path('',hpage,name="homepage"),
    path('about/',about,name="about"),
    path('nearby/',nearby,name="nearby-services")
]