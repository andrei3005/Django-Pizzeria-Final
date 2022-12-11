from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=20)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=40)

    class Meta: 
        verbose_name_plural='toppings'

    def __str__(self):
        return f"{self.topping_name[:50]}...."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review