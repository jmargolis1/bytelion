from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
	#return render(request, 'scratcher/home.html') 
	return HttpResponse('<h1> Bling Scratcher! </h1>')


def about(request):
	return HttpResponse('<h1> Scratcher About </h1>')