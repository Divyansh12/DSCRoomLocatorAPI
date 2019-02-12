from django.shortcuts import render
from .serializers import *
from .models import *
from decimal import Decimal
from django_filters import rest_framework as djfilters
from rest_framework.response import Response
from rest_framework import viewsets,permissions,filters,views

# Create your views here.

class CommenViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes  = (permissions.AllowAny,)
	filter_backends = (filters.OrderingFilter,filters.SearchFilter,djfilters.DjangoFilterBackend,)
	filterset_fields = '__all__'
	search_fields = '__all__'
	ordering_fields = '__all__'
	extra_permissions = None
	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		extra = []
		if self.extra_permissions is not None:
			extra = [permission() for permission in self.extra_permissions]
		return [permission() for permission in self.permission_classes]+extra


class DayViewSet(CommenViewSet):

   serializer_class = DaySerializer
   queryset = Day.objects.all()

class PeriodViewSet(CommenViewSet):

   serializer_class = PeriodSerializer
   queryset = Period.objects.all()

class BlockViewSet(CommenViewSet):

   serializer_class = BlockSerializer
   queryset = Block.objects.all()

class RoomNumberViewSet(CommenViewSet):

   serializer_class = RoomNumberSerializer
   queryset = RoomNumber.objects.all()

class RoomViewSet(CommenViewSet):

   serializer_class = RoomSerializer
   queryset = Room.objects.all()

class AvailabilityViewSet(CommenViewSet):

   serializer_class = AvailabilitySerializer
   queryset = Availability.objects.all()



