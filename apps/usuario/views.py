from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def usuario(request):
     return render(request,'usuario/index.html')
