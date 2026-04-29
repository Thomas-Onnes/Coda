from rest_framework import generics
from .models import Drink
from .serializer import DrinkSerializer
from django.shortcuts import render

class DrinkListCreateView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer