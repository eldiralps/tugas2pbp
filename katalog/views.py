from django.shortcuts import render
from wishlist.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html")
    