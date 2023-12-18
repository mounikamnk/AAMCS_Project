from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def secretary(request):
    return render(request,'secretary.html')

def apply(request):
    return render(request,'apply.html')

def management_consulting(request):
    return render(request,'management_consulting.html')

def cyber_sequirity(request):
    return render(request,'cyber_sequirity.html')

def statical_consultant(request):
    return render(request,'statical_consultant.html')

def tq(request):
    return render(request,'tq.html')