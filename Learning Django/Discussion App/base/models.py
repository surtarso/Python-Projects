from django.db import models
from django.contrib.auth.models import User


# Create your models here.


##------------------------------------------------TOPIC:
class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


##-------------------------------------------------ROOM:
class Room(models.Model): # ID is autogenerated

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #a topic can only have one room
    #a room can have many topics
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True) # can be empty
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # snapshot every time
    created = models.DateTimeField(auto_now_add=True) # snapshot once
    
    # classify in order (- to reverse, newest 1st)
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name



##------------------------------------------------MESSAGE:
## a user can have many messages
## a message can only have one user
class Message(models.Model):  # one to many relationship

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # if Room gets deleted, all children gets deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # snapshot every time
    created = models.DateTimeField(auto_now_add=True) # snapshot once

    class Meta:
       ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]  # limits message to 50 chars