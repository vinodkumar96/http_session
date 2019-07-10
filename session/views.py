from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def add (request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x+y
    request.session['z']= z
    request.session_expiry(30)
    return HttpResponse("data submited successfully")
def display (request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse(z)
    else:
        return render(request,'input.html')
