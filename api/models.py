from django.db import models

SIZE_CHOICES = sorted([('small', 'small'), ('medium', 'medium'), ('large', 'large')])
SHAPE_CHOICES = sorted([('regular', 'regular'), ('square', 'square')])


class Toppings(models.Model):
    topping_name = models.CharField(max_length=50)

    def __str__(self):
        return self.topping_name


class Pizza(models.Model):
    customer_name = models.CharField(max_length=100)
    size = models.CharField(choices=SIZE_CHOICES, default='medium', max_length=50)
    toppings = models.ManyToManyField(Toppings)
    shape = models.CharField(choices=SHAPE_CHOICES, default='regular', max_length=50)

    def __str__(self):
        return f"{self.size} size pizza ordered by {self.customer_name}"
