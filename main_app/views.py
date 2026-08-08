from django.http import HttpResponse
from .models import Item


def index(request):
  item_list = Item.objects.all() # alle Items fetchen
  # return HttpResponse("Hello World!")
  return HttpResponse(item_list) # returned die Items-Namen


def item(request):
  return HttpResponse("This is an item view.")
