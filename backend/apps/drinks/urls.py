from django.urls import path, include
from .views import DrinkListCreateView, DrinkUpdateDestroyView

urlpatterns = [
    path("drinks/", DrinkListCreateView.as_view()),
    path("drinks/<int:pk>", DrinkUpdateDestroyView.as_view())
]