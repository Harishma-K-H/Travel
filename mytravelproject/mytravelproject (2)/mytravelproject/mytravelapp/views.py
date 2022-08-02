from django.shortcuts import render
from .models import place,teams


def demo(request):
    obj=place.objects.all()

    obj3=teams.objects.all()
    return render(request,"index.html",{'result':obj,'results':obj3})

