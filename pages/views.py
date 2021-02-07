from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices
# Create your views here.

def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]

    context = {
        'listings':listings,
        'state_choices' : state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices
    }

    return render(request,'pages/index.html',context)

def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    context = {
        "realtors": realtor,
        "mvp_realtors" : mvp_realtor
    }
    return render(request,'pages/about.html',context)