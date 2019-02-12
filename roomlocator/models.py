from django.db import models
from django.contrib.auth.models import User
from django.core import validators

class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    def delete(self,*args, **kwargs):
        self.archived = True
        super().save(self,*args, **kwargs)
        super().save(*args, **kwargs)
    class Meta:
        abstract = True


class Day(CommonModel):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Period(CommonModel):
    time=models.TimeField()
    day=models.ForeignKey(
        Day,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}-{}'.format(self.day.name,self.time)

class Block(CommonModel):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class RoomNumber(CommonModel):
    number=models.CharField(max_length=3)
    
    def __str__(self):
        return self.number




class Room(CommonModel):
    number=models.ForeignKey(
        RoomNumber,
        on_delete=models.CASCADE
    )
    isLab=models.BooleanField(default=False)
    block=models.ForeignKey(
        Block,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}-{}'.format(self.block,self.number.number)



class Availability(CommonModel):
    isAvailable=models.BooleanField(default=False)
    room=models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    period=models.ForeignKey(
        Period,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}-{}-{}'.format(self.room,self.period,self.isAvailable)

    class Meta:
        unique_together= (("room","period"),)