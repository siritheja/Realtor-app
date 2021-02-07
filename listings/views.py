from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices,bedroom_choices,state_choices
# Create your views here.

def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listings = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing' : listings
    }
    return render(request,'listings/listing.html',context)

def search(request):    
    res_listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    keywords = request.GET['keywords']
    if keywords :
        res_listings = Listing.objects.filter(description__icontains=keywords).order_by('-list_date')

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            res_listings = Listing.objects.filter(city__iexact=city).order_by('-list_date')
    
    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            res_listings = Listing.objects.filter(state__iexact=state).order_by('-list_date')

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            res_listings = Listing.objects.filter(bedrooms__lte=bedrooms).order_by('-list_date')

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            res_listings = Listing.objects.filter(price__lte=price).order_by('-list_date')

    context = {
        'listings':res_listings,
        'state_choices' : state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'values' : request.GET
    }
    return render(request,'listings/search.html',context)