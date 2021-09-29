from django.shortcuts import render
from .models import *

# Create your views here.
def cars_view(request):
    featured_cars = Team.objects.all().order_by('created_date')


    template_name = 'cars/cars.html'
    context = {

                    }
    return render(request, template_name, context)
