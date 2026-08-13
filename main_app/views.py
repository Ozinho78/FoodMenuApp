from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ItemForm
from .models import Item


def index(request):
    # Getting items from the database
    item_list = Item.objects.all()  # alle Items fetchen
    # Creating context
    context = {
        # notwendig, damit Variable im HTML erkannt und gerendert wird
        'item_list': item_list
        # <QuerySet [<Item: Pizza>, <Item: Burger>, <Item: Burrito>, <Item: Cheesy Burger>]>
    }
    # return HttpResponse("Hello World!")
    # return HttpResponse(item_list) # returned die Item-Namen
    # schaut im Ordner templates/main_app nach dem HTML-Template
    # Passing the context object to the render method alogn with the template
    return render(request, "main_app/index.html", context)


def detail(request, id):
    # holt nur ein Item, dass der Id entspricht aus der DB
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    # return HttpResponse(f"This is the detail view for item with the id as {item}")
    return render(request, "main_app/detail.html", context)


def item(request):
    return HttpResponse("This is an item view.")


def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # zurück zur Index-Page
            return redirect('main_app:index')
        # <QueryDict: {'csrfmiddlewaretoken': ['Dd6YCim4EpBk4pPNmZdhj0ZvxFES1oP5kL0395uLtDZjRlPKQpN9OjV98FkNIIIt'], 'item_name': ['Pasta'], 'item_desc': ['Delicious pasta'], 'item_price': ['13'], 'item_image': ['pasta.jpg']}>
        # [14/Aug/2026 00:12:48] "POST /main_app/add/ HTTP/1.1" 200 795
        print("Post request is triggered")
        print(request.POST)

    context = {
        'form': form
    }
    return render(request, "main_app/item-form.html", context)
