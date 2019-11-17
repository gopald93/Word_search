from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import City
from rest_framework import generics
import csv
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from rest_framework.decorators import api_view
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

@api_view(['GET'])
def search_api(request):
    cities_list=[]
    return_dict={}
    if request.method == 'GET': 
        word = request.GET.get('word', '')
        cities_obj = City.objects.all()
        for data in cities_obj:
            cities_list.append((data.city_name,data.city_code))   
        demo_data=process.extract(word,cities_list,limit=25)
        for  data in demo_data:
            return_dict.update({data[0][0]:data[0][1]})
        return JsonResponse({"data":return_dict})   
    return JsonResponse({"message": "Hello, world!"})