from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def TSdashboard(request):
    return render(request,'TSdashboard.html')
def TStask(request):
    return render(request,'TStask.html')
def TSproject(request):
    return render(request,'TSproject.html')
def TSprojectdetails(request):
    return render(request,'TSprojectdetails.html')
def TSassigned(request):
    return render(request,'TSassigned.html')
def TSsubmitted(request):
    return render(request,'TSsubmitted.html')
def TSsucess(request):
    return render(request,'TSsucess.html')

# manager module
# Employee 

def Manager_index(request):
    return render(request,'Manager_index.html')
def Manager_employees(request):
    return render(request,'Manager_employees.html')
def Manager_tl(request):
    return render(request,'Manager_tl.html')
def Manager_tl_dashboard(request):
    return render(request,'Manager_tl_dashboard.html')

