from django.shortcuts import render, HttpResponse
from background_task import background 
from distributor.distributor_system import DistributorSystem as DS
# Create your views here.

@background(schedule=5)
def distributorStatus():
	DSobj = DS()
	DS.checkQueueStatus()

def backgroundViews():
	return HttpResponse("Background task of Queue system is running")
