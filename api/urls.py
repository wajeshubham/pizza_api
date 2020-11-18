from django.urls import path

from .views import PizzaListViewset, PizzaDeleteView,get_pizza_by_size,get_pizza_by_shape

urlpatterns = [
    path('', PizzaListViewset.as_view(), name="home"),
    path('delete/<int:pizza_id>/', PizzaDeleteView.as_view(), name="delete_order"),
    path('size/<str:size>/', get_pizza_by_size, name="delete_order"),
    path('shape/<str:shape>/', get_pizza_by_shape, name="delete_order"),
]
