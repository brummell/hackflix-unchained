# Create your views here.
from lists.models import Item
from django.shortcuts import render, redirect

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html')
