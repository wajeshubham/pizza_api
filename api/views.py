from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Pizza, Toppings
from .serializers import PizzaSerializer


class PizzaListViewset(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def post(self, request, *kwargs):
        pizza = Pizza.objects.create(customer_name=request.data['customer_name'],
                                     size=request.data['size'],
                                     shape=request.data['shape'])

        # here we are taking comma separated toppings name and splitting them at ',' and
        # creating list of the toppings name
        for i in request.data['toppings'].split(','):
            req_topping = get_object_or_404(Toppings, topping_name=i)
            pizza.toppings.add(req_topping)

        serializer = PizzaSerializer(pizza)
        data = {
            'pizza_order': serializer.data
        }

        return Response(data)


@api_view(['GET'])
def get_pizza_by_size(request, **kwargs):
    pizza = Pizza.objects.filter(size=kwargs.get('size'))
    serializer = PizzaSerializer(pizza, many=True)
    data = {
        f'{kwargs.get("size")}_size_pizzas': serializer.data
    }

    return Response(data)


@api_view(['GET'])
def get_pizza_by_shape(request, **kwargs):
    pizza = Pizza.objects.filter(shape=kwargs.get('shape'))
    serializer = PizzaSerializer(pizza, many=True)
    data = {
        f'{kwargs.get("shape")}_pizzas': serializer.data
    }

    return Response(data)


class PizzaDeleteView(generics.DestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def delete(self, request, **kwargs):
        pizza = get_object_or_404(Pizza, id=kwargs.get('pizza_id'))
        pizza.delete()
        data = {
            'response': 'order deleted successfully!'
        }
        return Response(data)
