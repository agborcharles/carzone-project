from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [

    path('', views.cars_view, name='cars'),
    #path('about/', views.about_view, name='about'),
    #path('contact/', views.contact_view, name='contact'),

]
