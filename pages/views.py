from django.shortcuts import render

# Create your views here.
def home_view(request):

    template_name = 'pages/home.html'
    context = {}
    return render(request, template_name, context)

def about_view(request):
    template_name = 'pages/about.html'
    context = {}
    return render(request, template_name, context)

def services_view(request):
    template_name = 'pages/services.html'
    context = {}
    return render(request, template_name, context)

def contact_view(request):
    template_name = 'pages/contact.html'
    context = {}
    return render(request, template_name, context)
