from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import prices_choices, bedroooms_choices, state_choices
from listings.models import Listings 
from realtors.models import Realtors



def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_publish= True)[:3]
   
    context = {
        'listings': listings,
        'state_choices': state_choices, 
        'prices_choices': prices_choices,
        'bedrooms_choices': bedroooms_choices
    }

    return render(request, "pages/index.html", context)

def about(request):
    #Get realtors
    realtors = Realtors.objects.order_by('-hire_date')

    #get MVP
    mvp_realtors = Realtors.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)
