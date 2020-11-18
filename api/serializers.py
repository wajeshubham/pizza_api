from rest_framework import serializers

from .models import Pizza, Toppings


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = "__all__"


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingsSerializer(many=True)

    class Meta:
        model = Pizza
        fields = "__all__"
