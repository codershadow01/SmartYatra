from django.urls import path
from . import views

urlpatterns = [
    path('planner/',views.planner,name="planner")
]