from django.shortcuts import render, redirect
from .models import *
from .forms import *
#from .forms import *

# Create your views here.

# When a URL request matches the pattern we just defined,
# Django looks for a function called index() in the views.py file

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')
    #return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    #pizzas = Pizza.objects.order_by('date_added')

    context = {'all_pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    #print(pizza)
    #toppings = Topping.objects.filter(pizza=pizza)
    toppings = Topping.objects.filter(pizza=pizza)

    #context = {'pizza':pizza, 'toppings':toppings}
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

        context = {'form':form, 'pizza':pizza}
        return render(request, 'pizzas/new_comment.html',context)