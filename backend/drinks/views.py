from rest_framework import viewsets
from .models import Drink
from .serializer import DrinkSerializer
from django.shortcuts import render

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer