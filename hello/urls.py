from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name="index" ),
    path("brien" , views.brien , name="brien"),
    path("<str:name>" , views.greeting , name="greeting")
]
