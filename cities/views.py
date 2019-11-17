from django.views.generic import TemplateView, ListView
import csv
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import City
from django.shortcuts import render
from .forms import ContactForm
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
def create(request):
    with open('/home/krishna/cushy_flask_data_center/city_data.csv','r') as second_file:
        city_file_obj = csv.DictReader(second_file)
        for city_data in city_file_obj:
            city_obj = City(city_name=city_data.get("city"), city_code=city_data.get("code"))
            city_obj.save()
    return HttpResponse("data is created successfully")    

def fuzzy_huzzy_solution(city_name):
    cities_list=[]
    return_dict={}
    cities_obj = City.objects.all()
    for data in cities_obj:
        cities_list.append((data.city_name,data.city_code))   
    demo_data=process.extract(city_name,cities_list,limit=25)
    for  data in demo_data:
        return_dict.update({data[0][0]:data[0][1]})
    return return_dict       
def search(request):
    result_dict={}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city_name']
            result_dict=fuzzy_huzzy_solution(city_name)
            return render(request, 'cities/form_index.html', {'form': form,'result_dict':result_dict})
    else:
        form = ContactForm()
    return render(request, 'cities/form_index.html', {'form': form})