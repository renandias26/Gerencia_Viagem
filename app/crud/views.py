from django.shortcuts import render, redirect
from .models import Travel, Destiny

# Create your views here.
def home(req):
    data = Travel.objects.all()
    return render(req, "home.html", {"travels": data})

def update(req, id):
    data = Travel.objects.get(id=id)
    dest = Destiny.objects.filter(travel=data)
    return render(req, "update.html", {"travel": data, "dest": dest})

def delete(req, id):
    data = Travel.objects.get(id=id)
    data.delete()
    return redirect(home)

def create(req):
    return render(req, "create.html")

def createTravel(req):
    destiny = req.POST.get('destiny')
    name = req.POST.get('name')
    value = req.POST.get('value')
    dateLeave = req.POST.get('dateLeave')
    dateCome = req.POST.get('dateCome')
    data = Travel.objects.create(
        name=name, 
        value=value,
        dateLeave=dateLeave,
        dateCome=dateCome
    )
    data.addDestiny(destiny)
    
    return redirect(home)

def updateTravel(req, id):
    data = Travel.objects.get(id=id)

    name = req.POST.get('name')
    value = req.POST.get('value')
    dateLeave = req.POST.get('dateLeave')
    dateCome = req.POST.get('dateCome')

    data.name=name
    data.value=value
    data.dateLeave=dateLeave
    data.dateCome=dateCome

    data.save()
    return redirect(home)

def deleteDestiny(req, id):
    data = Destiny.objects.get(id=id)
    travelId = data.travel
    dest = Destiny.objects.filter(travel=data.travel)

    if dest.count() == 1:
        return redirect(update, id=travelId.id)

    data.delete()
    return redirect(update, id=travelId.id)

def addDestiny(req, id):
    data = Travel.objects.get(id=id)
    destinyName = req.POST.get('destinyName')
    data.addDestiny(destinyName)
    return redirect(update, id=id)