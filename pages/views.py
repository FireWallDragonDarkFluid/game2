from django.shortcuts import render
from listings.models import Listing
from listings.choices import game_type,game_price

def index(request):
    listings = Listing.objects.all()[:3]
    context = {
        'listings':listings,
        'game_type':game_type,
        'game_price':game_price
    }
    return render(request,'pages/index.html',context)