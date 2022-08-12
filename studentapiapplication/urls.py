from django.urls import path
from . import views

app_name = "studentapiapplication"

urlpatterns = [
    path("gabriel/", views.student_list, name="myapifunction")
]