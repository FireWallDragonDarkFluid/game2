from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import game_type,game_price
from .models import Listing
def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings':paged_listings
    }
    return render(request,'listings/listings.html',context)
def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request,'listings/listing.html',context)
def search(request):
    queryset_list = Listing.objects.all()

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #game_type1
    if 'type1' in request.GET:
        type1 = request.GET['type1']
        if type1:
            queryset_list = queryset_list.filter(tag__icontains=type1)
    #game_type2
    if 'type2' in request.GET:
        type2 = request.GET['type2']
        if type2:
            queryset_list = queryset_list.filter(tag__icontains=type2)   
    #game_price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)    
    #game_name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)        

    context = {
        'game_type':game_type,
        'game_price':game_price,
        'listings':queryset_list
    }

    return render(request,'listings/search.html',context)