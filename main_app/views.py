from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def index(request):
  item_list = Item.objects.all() # alle Items fetchen
  # return HttpResponse("Hello World!")
  # return HttpResponse(item_list) # returned die Item-Namen
  return render(request,"main_app/index.html") # schaut im Ordner templates/main_app nach dem HTML-Template


def item(request):
  return HttpResponse("This is an item view.")
