from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Person():
    pass
def home(request):
    t1= Person()
    t1.title = 'Payal'
    t1.desc = "National Cadet Corps"
    t1.button= 5
    t2 = Person()
    t2.title = 'hetvi'
    t2.desc = "Programmer 3 star"
    t2.button= 10
    l=[t1,t2]

    return render(request,'home.html',{"data":l})
def result(request):
    x=int(request.POST['num1'])
    y=int(request.POST['num2'])
    res= x+y
    return render(request, 'result.html',{"result": res})