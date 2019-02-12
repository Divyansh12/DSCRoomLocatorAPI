import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import *


class DayType(DjangoObjectType):
    class Meta:
        model=Day


class PeriodType(DjangoObjectType):
    class Meta:
        model=Period


class BlockType(DjangoObjectType):
    class Meta:
        model=Block

class RoomNumberType(DjangoObjectType):
    class Meta:
        model=RoomNumber

class RoomType(DjangoObjectType):
    class Meta:
        model=Room

class AvailabilityType(DjangoObjectType):
    class Meta:
        model= Availability


class Query(object):
    all_availability = graphene.List(AvailabilityType)
    all_room = graphene.List(RoomType)
    
    # customuser = relay.Node.Field(CustomUserType)
    # all_customuser = DjangoFilterConnectionField(CustomUserType)

    # participated = relay.Node.Field(ParticipatedType)
    # all_participated = DjangoFilterConnectionField(ParticipatedType)

    def resolve_all_availability(self,info,**kwargs):
        return Availability.objects.all()

    def resolve_all_room(self, info, **kwargs):
        return Room.objects.all()