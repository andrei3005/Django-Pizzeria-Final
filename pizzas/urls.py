#path function needed when mapping URLs to views
from django.contrib import admin
from django.urls import path, include

#dot tells Python to import the views.py module from
#same directory as the current urls.py module
from . import views

#variable app_name helps Django distinguish this urls.py frile from 
# files of the same name in other apps within the project
app_name = 'pizzas'

#variable urlpattens in this module is a list of individual pages
# that can be requested from the pizzas app

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
]
'''
urlpatterns = [ 
    #first argument is empty string ('') which matches the
    # base URL - http://localhost:8000/. the second argument specifies
    # the function name to call in views.py. 
    #the third argument provides 
    # the name 'index' for this URL pattern to refer to it later
    path('',views.index, name='index'),
    path('pizzas',views.pizzas,name='pizzas')
    path('', include('Pizzeria.urls')),
    #path('',include('pizzas.urls'))
    #path('users/', include('users.urls')),
]
'''
'''
urlpatterns = [

    path('',views.index, name='index'),
    path('pizzas',views.pizzas,name='pizzas')

]
'''
