from django.urls import path
from . import views

urlpatterns = [
    path('planner/',views.planner,name="planner"),
    path('',views.hpage,name="homepage"),
    path('about/',views.about,name="about")
]