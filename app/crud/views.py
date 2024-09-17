from django.shortcuts import render, redirect
from .models import Travel

# Create your views here.
def home(req):
    data = Travel.objects.all()
    return render(req, "home.html", {"travels": data})

def save(req):
    dataName = req.POST.get('name')
    dataAge = req.POST.get('age')
    Travel.objects.create(name=dataName, age=dataAge)
    return redirect(home)


def edit(req, id):
    data = Travel.objects.get(id=id)
    return render(req, "update.html", {"person": data})

def update(req, id):
    print(id)
    dataName = req.POST.get('name')
    dataAge = req.POST.get('age')

    data = Travel.objects.get(id=id)

    data.name = dataName
    data.age = dataAge
    data.save()
    return redirect(home)

def delete(req, id):
    data = Travel.objects.get(id=id)
    data.delete()
    return redirect(home)

def create(req):
    return render(req, "create.html")