#from django.conf.urls import url
from django.urls import path, include

from .views import *


urlpatterns = [ 
    path('divisions/', DivisionView.as_view()),
    path('districts/', DistrictView.as_view()),
  
    path('getdivisiondistrict/', DistrictDivisonView.as_view()),
    path('getarea/', AreaView.as_view()),
    path('getdistrictarea/', DistrictAreaView.as_view()),


]