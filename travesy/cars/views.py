from django.shortcuts import render
from .models import *

from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

# def cars(request):
#     car_type=Car.objects.all()
#     context={'car_type':car_type,}
#     return render(request, 'cars/car.html', context)


def car_list(request):
    car_type = Car.objects.all()
    if request.method == "GET":
        cn = request.GET.get("car_name")
        if cn:
            car_type = Car.objects.filter(name__icontains=cn)
    return render(request, 'cars/car.html', {'car_type':car_type})