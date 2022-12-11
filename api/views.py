from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from .models import Division, District, Area
from .serializers import DivisionSerializer, DistrictSerializer, AreaSerializer
# Create your views here.


class DivisionView(APIView):
    def get(self, request):
        divisions = Division.objects.all()
        serializer = DivisionSerializer(divisions, many=True)
    
        return Response(serializer.data)

class DistrictView(APIView):
    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)
    
class AreaView(APIView):
    def get(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

class DistrictDivisonView(APIView):
    def get(self, request):
        
        id = request.GET['id']
        print(id)
        district = District.objects.filter(division_id=id)
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)

class AreaView(APIView):
    def get(self, request):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

class DistrictAreaView(AreaView):
    def get(self, request):
        id = request.GET['id']
        area = Area.objects.filter(district_id=id)
        serializer = DistrictSerializer(area, many=True)
        return Response(serializer.data)