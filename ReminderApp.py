from django.shortcuts import render
from django.http import HttpResponse
def index(index):
	return HttpResponse("Hello World!")