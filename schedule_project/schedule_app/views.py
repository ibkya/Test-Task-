from django.shortcuts import render

from rest_framework import viewsets
from .models import TimeSlot
from .serializers import TimeSlotSerializer
from rest_framework.permissions import IsAuthenticated

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated]

