from django.shortcuts import render
from .merger_system import MergerSystem
from django.http import HttpResponse
from .models import OutputTable
# Create your views here.


def callMerger(request):
    MS=MergerSystem()
    MS.add_to_db()
    return HttpResponse('added to db')

def callPrinter(request):
    outp = OutputTable.objects.all()
    for o in outp:
        print(o.ox1+" "+o.ox2+" "+o.ox3+" "+o.ox4+" "+o.ox5+" "+o.oy1+" "+o.oy2+" "+o.oy3+" "+o.oy4+" "+o.oy5+" "+str(o.otaskpath)+" "+o.otaskid)
    return HttpResponse('printed the db')
