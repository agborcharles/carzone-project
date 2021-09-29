from django.shortcuts import render
from .models import *
from cars.models import *

# Create your views here.
def home_view(request):
    our_team = Team.objects.all().order_by('created_date')
    featured_cars = Car.objects.order_by('created_date').filter(is_feautred=True)


    template_name = 'pages/home.html'
    context = {
                    'our_team':our_team,
                    'featured_cars':featured_cars
                    }
    return render(request, template_name, context)

def about_view(request):
    our_team = Team.objects.all().order_by('created_date')


    template_name = 'pages/about.html'
    context = {
                    'our_team':our_team
                    }

    return render(request, template_name, context)

def services_view(request):
    template_name = 'pages/services.html'
    context = {}
    return render(request, template_name, context)

def contact_view(request):
    template_name = 'pages/contact.html'
    context = {}
    return render(request, template_name, context)
