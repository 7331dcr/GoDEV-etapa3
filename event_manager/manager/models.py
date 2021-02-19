from django.db import models

class Event_room(models.Model):
    name = models.TextField(blank=False)
    capacity = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Coffee_space(models.Model):
    name = models.TextField(blank=False)
    capacity = models.IntegerField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Attendee(models.Model):
    name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    event_room = models.ForeignKey("Event_room", null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)