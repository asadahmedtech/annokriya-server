from django.shortcuts import render

# Create your views here.
from .models import Dashboard
from django.http import HttpResponse
# Create your views here.

def display(request):
    dash = Dashboard.objects.filter(user=request.user)

    for d in dash:
        print(str(d.user)+" "+str(d.pending)+" "+str(d.correct)+" "+str(d.wrong)+" "+str(d.credits))
        return HttpResponse(str(d.user)+" "+str(d.pending)+" "+str(d.correct)+" "+str(d.wrong)+" "+str(d.credits))
    return HttpResponse('ok')
