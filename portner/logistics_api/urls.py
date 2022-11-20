from django.urls import path
from logistics_api import views

urlpatterns = [
    path('add', views.assetrequester),
    path('retrieve', views.retrieveRequester),
    path('riderTravelInfo', views.riderTravelInfo),
    path('matchRequests', views.matchRequests),
    path('apply', views.apply)
]