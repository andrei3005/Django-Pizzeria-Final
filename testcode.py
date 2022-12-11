import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza


pizzas = Pizza.objects.all()

print(pizzas)

for p in pizzas:
    print(p)
    print(p.pizza_name)