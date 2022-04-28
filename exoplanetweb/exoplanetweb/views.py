from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def home(request):
	return render(request,'home.html')

def features(request):
	return render(request,'features.html')

def about(request):
	return render(request,'about.html')

def output(request):
	return render(request,'output.html')


def external(request):
	#inp= request.POST.get('param')
	out=run([sys.executable,'F:\\BE\\PROJECT\\ExoPlanet-Detection-main\\main.py'],shell=False,stdout=PIPE) #To run external python script
	print(out) 

	return render(request,'output.html',{'data1':out.stdout}) #To print the output from external python script onto website