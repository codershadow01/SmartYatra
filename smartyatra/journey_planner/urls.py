from django.urls import path
from .views import planner,hpage,about

urlpatterns = [
    path('planner/',planner.as_view(),name="planner"),
    path('',hpage,name="homepage"),
    path('about/',about,name="about")
]