from django.db import models

class Event_room(models.Model):
    name = models.TextField(blank=False)
    capacity = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id:{self.id} name:{self.name} capacity:{self.capacity} timestamp:{self.timestamp.strftime("%A, %d. %B %d/%m/%Y %I:%M %p")}'


class Coffee_space(models.Model):
    name = models.TextField(blank=False)
    capacity = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'id:{self.id} name:{self.name} capacity:{self.capacity} timestamp:{self.timestamp.strftime("%A, %d. %B %d/%m/%Y %I:%M %p")}'


class Attendee(models.Model):
    name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    event_room = models.ForeignKey("Event_room", null=True, blank=True, on_delete=models.SET_NULL)
    coffee_space = models.ForeignKey("Coffee_space", null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id:{self.id} name:{self.name} last_name:{self.last_name} event_room:{self.event_room} coffee_space:{self.coffee_space} timestamp:{self.timestamp.strftime("%A, %d. %B %d/%m/%Y %I:%M %p")}'