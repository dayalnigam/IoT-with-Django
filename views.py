from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Sensor_data.models import Sensor_Data
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
def mydata(request):

	url="http://192.168.43.45/"
	html_content = requests.get(url).text
	# Parse the html content
	soup = BeautifulSoup(html_content, "lxml")
	#print(soup.prettify()) # print the parsed data of html
	data= soup.find('p').getText()
	all_data = Sensor_Data.objects.all().order_by("-id")
	print(data)
	s=Sensor_Data(LDR=data)
	s.save()
	return render(request,"Data.html",{"messages":all_data})

def myplot(request):
	labels = []
	data =[]
	queryset = Sensor_Data.objects.all()
	for sensor in queryset:
		labels.append(sensor.id)
		data.append(sensor.LDR)
	return render(request,"myindex.html",{"labels":labels,"data":data,})

def home(request):
	return render(request,"home.html")







    	
